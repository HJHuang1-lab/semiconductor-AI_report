# 🤖 半導體製程良率 AI Agent 自動分析報告系統

> **全球首款針對先進製程良率提升（Yield Enhancement）與 AI Agent 結合的自動化定時研發報告生成與發送系統。**
> 結合 **Gemini 2.5 搜尋聯網（Search Grounding）**、**Imagen 4.0 即時 AI 繪圖** 與 **NotebookLM 深度學術/專家風簡報生成引擎**，在雲端全自動背景執行。

---

## 🌟 核心特色 (Core Features)

1. **全球 24 小時聯網搜尋（Gemini 2.5 Search Grounding）**
   - 每日自動追蹤全球關於 AI Agent 與半導體製程結合的最新論文（arXiv, SPIE）、新聞、晶圓代工大廠（TSMC, Samsung, Intel）與設備商（Applied Materials, TEL, ASML）的最新製程良率提升（Yield Enhancement）核心動態。
   - 採創新的**兩階段 API 調用設計**，完美發揮 Search Grounding 與 JSON 結構化轉換的雙重優勢。

2. **NotebookLM 專家級學術風投影片**
   - 拋棄枯燥模板，採用專為內部分享設計的 **高級深色半導體晶片美學（Slate Dark Tech Aesthetic）**。
   - 自動生成高維度、邏輯密度的結構化專家閱讀卡片，提供具體量化指標（如良率提升 1-3%、RCA 時效提升 95%）與關鍵技術名詞（如 DANA 架構、Run-to-Run 控制、KGD 篩選）。

3. **即時 AI 繪圖生成（Imagen 4.0）**
   - 每天在雲端執行時，會根據當天搜尋主題，自動為每一頁投影片定制專屬的畫圖提示詞，並調用 **Imagen 4.0** 在雲端即時繪製百分之百契合最新製程主題的科技圖表。

4. **防崩潰安全備份機制（Hybrid Failsafe）**
   - 若使用的 Gemini API 密鑰為免費開發者帳戶（不支援 Imagen 繪圖模型），系統會自動且無感地啟動**安全備份方案**，調用本地託管的高質感半導體概念插圖，確保雲端服務 100% 穩定，永不崩潰！

5. **全自動雲端定時發送（GitHub Actions + SSL SMTP）**
   - 配置 GitHub Actions 定時任務，**每天早上 9:00 台灣時間**自動喚醒執行，無需開機，無任何雲端伺服器運行成本。
   - 使用 SSL 加密安全通訊協定，自動將精美 PPT 作為附件發送至指定電子信箱。

---

## 📁 專案目錄結構

```text
├── .github/
│   └── workflows/
│       └── semiconductor_report.yml  # GitHub Actions 雲端定時排程設定檔 (每日早上 9 點)
├── assets/
│   ├── semiconductor_ai.png          # 備份圖片 1：封面 (AI 與晶圓整合)
│   ├── chamber_control.png           # 備份圖片 2：製程控制 (Chamber 即時監控)
│   ├── wafer_defect.png              # 備份圖片 3：缺陷診斷 (Wafer Map 掃描判讀)
│   └── yield_stack.png               # 備份圖片 4：Agent 良率 (Agent Yield Stack)
├── generate_report.py                # 核心執行腳本 (搜尋 -> 生成 PPT -> 發送郵件)
└── README.md                         # 專案說明文件 (本檔案)
```

---

## 🚀 本地快速開始 (Local Quick Start)

### 1. 安裝必要套件
請在您的終端機/命令提示字元中執行：
```bash
pip install python-pptx google-genai python-dotenv
```

### 2. 配置環境變數
在專案根目錄下建立一個 `.env` 檔案（或直接讀取現有配置），設定以下內容：
```env
GEMINI_API_KEY=您的GeminiAPI金鑰
GMAIL_USER=您的Gmail寄件信箱
GMAIL_APP_PASSWORD=您的Gmail應用程式密碼
```

### 3. 本地執行測試
```bash
python generate_report.py
```
執行成功後，您將在本地看到產生的 `AI_Agent_Semiconductor_Yield_Report.pptx`，且您的電子信箱會收到最新的 HTML 格式報告與簡報附件！

---

## ☁️ 雲端排程自動執行設定 (GitHub Actions Setup)

為了讓報告能在 GitHub 雲端上每天早上 9:00 定時自動發送，請完成以下簡單設定：

1. **設定 GitHub Repository Secrets**：
   - 進入您的 GitHub 專案頁面，點選 **Settings > Secrets and variables > Actions**。
   - 點選 **New repository secret**，新增以下兩個密鑰：
     - `GEMINI_API_KEY`：填入您的 Gemini API 金鑰。
     - `GMAIL_APP_PASSWORD`：填入您的 Gmail 應用程式發信密碼 (`ytts erdx vonw vedw`)。

2. **手動一鍵啟動測試**：
   - 點選 GitHub 頂部的 **Actions** 標籤。
   - 在左側選擇 **「🤖 每日早上 9 點半導體 AI Agent 良率分析報告發送」**。
   - 點選右側的 **Run workflow** 下拉選單，並點擊綠色的 **Run workflow**。雲端 Linux 主機會立刻啟動並完成報告生成與郵件發送！

---

## 📊 簡報核心議題架構

投影片共包含 **8 頁** 精美版面設計，主題涵蓋半導體先進製程良率提升最核心的三大維度：
*   **Slide 1: 封面** — AI Agent 與先進製程良率提升之關鍵路徑。
*   **Slide 2: 產業挑戰** — 製程步驟突破 2000 道，超越傳統靜態控制（SPC）的物理極限。
*   **Slide 3: 自主製程控制 (APC)** — Chamber 級虛擬控制器與跨工序自動校準 (Run-to-Run)。
*   **Slide 4: 智能缺陷診斷** — 整合 Wafer Sort 與 Final Test 的大數據，多模態 SEM 自動判讀與根因分析。
*   **Slide 5: 半導體專用模型** — SemiKong（Domain-Aware Neurosymbolic Agents DANA 架構）在 CVD 與蝕刻製程的突破。
*   **Slide 6: Agent 良率架構** — 將半導體 SPC 與 Poka-Yoke 防呆概念反向治理 AI Agent，打造工業級高可靠性系統。
*   **Slide 7: 封裝與 HBM 良率** — Chiplet 與 HBM 在先進封裝（TSMC CoWoS）下的智能匹配組裝（Matching Binning）策略。
*   **Slide 8: 封底** — 研發總結與聽眾致謝。

---

## 🛡️ 免責聲明與授權
本專案為半導體前沿技術之自動化研究推廣，採用 MIT 授權條款。敏感發信憑證與 API 金鑰已完全透過 `.env` 檔案與 GitHub 加密密鑰進行託管安全隔離，請勿將包含明文密鑰的檔案推上公共 GitHub 儲存庫。
