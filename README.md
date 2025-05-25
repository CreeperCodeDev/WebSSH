# WebSSH

一個具有現代化UI的WebSSH終端機應用程式，支援Windows、Linux和macOS系統。

## 功能特點

- macOS風格的視窗界面
- 深色/淺色主題切換
- 自定義端口配置
- 跨平台支援
- 即時命令執行
- 響應式設計
- Docker支援

## 快速開始

### 使用 Docker（推薦）

1. 直接運行（使用預設端口5000）：
```bash
docker run -d -p 5000:5000 --name webssh --privileged -v /:/host:ro ghcr.io/[您的GitHub用戶名]/webssh:latest
```

2. 使用自定義端口：
```bash
docker run -d -p 8080:8080 -e PORT=8080 --name webssh --privileged -v /:/host:ro ghcr.io/[您的GitHub用戶名]/webssh:latest
```

3. 使用 Docker Compose：
```bash
docker-compose up -d
```

### 手動安裝

1. 確保已安裝Python 3.7或更高版本
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```

3. 運行應用程式：
   ```bash
   python app.py
   ```

## 使用說明

1. 首次運行時，程式會詢問您要使用的端口號
2. 在瀏覽器中訪問 `http://localhost:<端口號>`
3. 點擊右上角的月亮/太陽圖標可以切換深色/淺色主題

## Docker 部署說明

### 從 Docker Hub 拉取

```bash
docker pull ghcr.io/[您的GitHub用戶名]/webssh:latest
```

### 構建自己的映像

1. 克隆倉庫：
```bash
git clone https://github.com/[您的GitHub用戶名]/webssh.git
cd webssh
```

2. 構建映像：
```bash
docker build -t webssh .
```

3. 運行容器：
```bash
docker run -d -p 5000:5000 --name webssh --privileged -v /:/host:ro webssh
```

## 注意事項

- 請確保您有適當的權限執行命令
- 建議在安全的網絡環境中使用
- 端口配置文件(port.yml)會在首次運行時自動創建
- Docker部署需要特權模式來執行命令
- 主機根目錄以只讀模式掛載，確保安全性

## 安全性建議

1. 在生產環境中使用時，建議：
   - 設置訪問密碼
   - 使用 HTTPS
   - 限制可執行的命令
   - 使用非特權用戶運行容器

2. 定期更新映像以獲取安全修復：
```bash
docker pull ghcr.io/[您的GitHub用戶名]/webssh:latest
```

## 貢獻

歡迎提交 Pull Request 或開 Issue 來改進這個專案。 