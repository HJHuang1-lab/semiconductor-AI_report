import http.server
import socketserver
import webbrowser
import sys
import os

# Configure stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

# Ensure we are in the correct directory of the workspace
workspace_dir = r"E:\Python檔案\GitHub research\AI agent research"
os.chdir(workspace_dir)

print("🚀 正在啟動本地 Web 伺服器來載入簡報模擬器...")
print("💡 這將 100% 解決瀏覽器因安全政策 (CORS/Mixed Content) 限制無法讀取地端 API 的問題！")

try:
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        url = f"http://127.0.0.1:{PORT}/SOP_to_Agentic_Workflow_Video_Simulator.html"
        print(f"\n🔗 伺服器已成功在 Port {PORT} 監聽！")
        print(f"👉 請開啟瀏覽器訪問：{url}")
        print("📢 提示：請保持此視窗開啟，不要關閉。")
        
        # Automatically open in user's default browser
        webbrowser.open(url)
        
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 伺服器已手動關閉。")
except Exception as e:
    print(f"\n❌ 啟動伺服器失敗：{e}")
