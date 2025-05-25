import os
import yaml
import platform
import subprocess
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, async_mode='threading')

def get_default_port():
    # 優先使用環境變數中的端口
    if 'PORT' in os.environ:
        return int(os.environ['PORT'])
    # 其次使用配置文件
    if os.path.exists('port.yml'):
        with open('port.yml', 'r') as f:
            config = yaml.safe_load(f)
            return config.get('port', 5000)
    return 5000

def save_port(port):
    with open('port.yml', 'w') as f:
        yaml.dump({'port': port}, f)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('connection_response', {'data': 'Connected'})

@socketio.on('command')
def handle_command(data):
    command = data.get('command', '')
    try:
        if platform.system() == 'Windows':
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        else:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                executable='/bin/bash'
            )
        
        stdout, stderr = process.communicate()
        emit('command_response', {
            'stdout': stdout,
            'stderr': stderr,
            'returncode': process.returncode
        })
    except Exception as e:
        emit('command_response', {
            'stderr': str(e),
            'returncode': 1
        })

if __name__ == '__main__':
    port = get_default_port()
    if not os.path.exists('port.yml') and 'PORT' not in os.environ:
        print(f"請輸入要使用的端口號（預設：{port}）：")
        user_port = input().strip()
        if user_port:
            try:
                port = int(user_port)
                save_port(port)
            except ValueError:
                print("無效的端口號，使用預設端口")
    
    print(f"WebSSH 服務器運行在 http://0.0.0.0:{port}")
    socketio.run(app, host='0.0.0.0', port=port, debug=False) 