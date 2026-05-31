import requests
import json
import sys
import os

# Configure stdout to UTF-8 to prevent encoding errors on Windows
sys.stdout.reconfigure(encoding='utf-8')

# ──────────────────────────────────────────────────────────────────────
# 💡 ELEVENLABS 聲音複製一鍵合成腳本說明
# ──────────────────────────────────────────────────────────────────────
# 1. 請先前往 https://elevenlabs.io/ 註冊一個免費帳戶。
# 2. 在 "Voices" -> "Instant Voice Cloning" 中上傳我們為您做好的 "語音_260531_153027.wav"。
# 3. 取得您的 xi-api-key (點選右上角頭像 -> Profile -> API Key)。
# 4. 取得您的 Voice ID (在 Voice 詳情中點選 ID 複製)。
# 5. 將金鑰與 ID 填入下方變數中，然後執行此腳本！
# ──────────────────────────────────────────────────────────────────────

API_KEY = "您的_ELEVENLABS_API_KEY_填在這裡"
VOICE_ID = "您的_CLONED_VOICE_ID_填在這裡"

# Slide 4 到 Slide 9 的完整口播稿文案
slides_text = {
    4: (
        "好，現在我們已經搞清楚定義，也知道為什麼不能用整包丟的 Mega Agent 了。"
        "那對技術或非技術人員來說，我們到底要怎麼動手？"
        "第一步，叫做格式標準化。相信我，大多數人的第一步就做錯了。"
        "他們直接把給人看的 Word 檔丟給 AI，這對 Agent 來說就是一坨非結構化的文字，它在跑的時候一定會漏東漏西。"
        "在標準化裡，我們要做三件事：第一是參數化。你不要在 SOP 裡寫死說一定要用 normal 模式。你要把這些寫死的東西改成 mode、temperature 這種變數，讓你的 SOP 變成一個模板，每次呼叫時可以根據實際情況帶入不同的值，這才叫容錯率！"
        "第二是引入 RFC 2119 規範。你必須強制把規則強度想清楚：哪些是 MUST——Agent 絕對不能妥協、一定要做的硬性限制；哪些是 SHOULD——建議作法，如果 Agent 不做，必須在 Log 中明確解釋理由；哪些是 MAY——Agent 可以根據 context 自主判定。"
        "第三是 Markdown 結構化。用 Markdown 把 Parameters、Steps、Error Handling 這些區塊清清楚楚地切開。這不僅是給人看的，更是為了方便後面塞入 MCP 等標準接口，直接當作 Agent 的行為特徵規格書。"
    ),
    5: (
        "標準化做好、合約立好之後，接下來就進入整個工作流的核心大腦——任務拆解與連結。"
        "在設計時，這個 Skill 的『防守範圍』要拆多大，是生死關鍵！防守範圍如果太大，容易樣樣通，但樣樣做得差強人意；防守範圍太小，又變成 Agent 每走一步都要回來讀 Skill、問人類，簡直像在帶幼稚園小孩。"
        "我們的核心原則是：以具備『獨立產出』作為單一 Skill 的防守防線，並將整個流程 Decompose 成多個獨立管道步驟（Pipeline Steps）。"
        "為什麼我一直強調『獨立』這兩個字？因為這奠定了後續所有的維護好處。如果分類步驟有 bug，你只需要回去修改分類那個 Skill 的 SOP Markdown 就好，後面設定機器、草擬回覆的邏輯完全不受影響，壞哪裡改哪裡！"
        "那麼，這些獨立的 Agent 或節點之間，要靠什麼串接呢？"
        "記住，絕對不是靠 LLM 之間逆天的心電感應，而是靠清清楚楚定義的 Artifacts，也就是結構化的 JSON 檔案！前一個節點的 JSON 輸出，直接完美對接下一個節點的輸入。數據流清澈透明，這就是生產級系統的精髓。"
    ),
    6: (
        "走到這裡，很多人以為自己做完架構就可以去喝咖啡了。但我跟你保證，你第一版設計出來的流程，拿去跑絕對會垮掉！"
        "為什麼我可以這麼篤定？因為一個非常關鍵的觀念，叫做默會知識，也就是內隱知識。"
        "所謂默會知識，就是指那些存在於你的大腦或身體記憶中、難以用言語或圖表精確表達的潛規則。比如你在 SOP 裡寫『洗衣服』，你可能忘了寫羊毛衣不能烘、白襯衫要分開。這些潛規則你自己是不會發現的，直到 Agent 實際去跑、去出錯、把你的高檔毛衣烘到縮水穿不下時，你才會一拍腦袋說：『啊！這條規則我忘了寫進去！』"
        "所以，雙向開發的本質，就是跟 Agent 一起實跑、一起踩坑、一起迭代的過程。"
        "不要嘗試關在房間裡閉門造車兩個月，去憋一個所謂的完美 SOP。我們應該秉持 Scrum 的敏捷精神『小步快跑』：兩天之內寫出一個很粗糙但能動的 v1.0，然後一個禮拜之內狂跑 50 次測試！每次它踩到一個你沒想到的 edge case，你就回頭在 SOP 裡補上一條 MUST 或 SHOULD 防禦規則。幾輪下來，這份 SOP 就會被迭代到無比強壯，能應對 95% 以上的真實場景！"
    ),
    7: (
        "流程都穩定了，最後一步就是接通真實世界，給我們的 Agent 裝上手和腳，這就是整合與執行環境。"
        "在以前，要把 Agent 整合進公司內部，是個無比痛苦的過程。你得為 A 公司寫一套 Slack 串接，為 B 公司寫一套 Jira 串接。幸好，現在我們有了 MCP——Model Context Protocol。我最喜歡把 MCP 比喻成 AI 世界的 USB-C！"
        "就像 USB-C 出現之後，你不需要為滑鼠、手機、筆電準備十幾種轉接線一樣；只要支援 MCP 協定，你的 Slack 工具、資料庫工具，不管是 Claude、ChatGPT 還是 Cursor，都可以隨插即用，一次開發，終身受用。"
        "接通工具之後，千萬不要忘記設計最後一道安全防線：Human-in-the-Loop，也就是人工確認節點。"
        "任何自動化工作流不論多成熟，一定會遇到 Agent 無法判斷的極端狀況。這時如果你讓 Agent 硬著頭皮去亂猜，風險高到你根本不敢讓它上線生產環境。我們的作法是：在所有涉及大額財務、主權限變更或大量刪除等高風險決策前，強制設置 MUST 暫停點。Agent 必須停下來在 Slack 發送確認，等待人類主管親自審查並按下 Approve。"
        "這就叫人類掌舵，AI 划槳。既保證了極致的安全，又把所有重複、機械、無聊的體力活，100% 委派給了 AI！"
    ),
    8: (
        "剛聽剛剛那些理論，你可能會覺得有點抽象。那我們直接套用一個真實的公司場景來演練：內部請求自動分類與 triage 系統。"
        "想像你在一個 200 人的公司，每天都會收到成百上千條透過 Slack、Email 或表單丟進來的雜事請求。比如：『我要申請權限』、『這發票可否報帳』。這個流程很重複、很煩，但每天都要做，最適合用 Agent 解決！"
        "首先，Step 1：標準化。"
        "我們寫一份 `INTERNAL_REQUEST_TRIAGE` 的 SOP。參數化輸入 raw_text 和 employee_id。在 SOP 裡硬性規定：Agent MUST 先檢查員工身分、MUST 把請求歸入 IT、HR 或 Finance、SHOULD 判斷優先級。"
        "接著，Step 2：任務拆解。"
        "我們把這個任務攔腰折半，拆成兩個職責極度單一的 Skill：第一個叫 `request-triage`，它只專注做一件事：讀入請求，吐出一份結構化 JSON。JSON 裡寫明分類、assignee 和需不需要澄清。第二個叫 `reply-drafting`，它也只專注一件事：讀入剛剛那份 JSON，然後草擬回覆。如果 JSON 裡的 `needs_clarification` 為 true，它就 MUST 產生 2 到 3 個釐清問題。"
        "你看，這兩個 Skill 之間沒有任何黏滯性。今天如果你想把郵件的口吻從『嚴肅』改成『活潑』，你只需要改技能 B 的 SOP 即可，技能 A 的分類邏輯完全不用重新測試，這就是拆解的威力！"
    ),
    9: (
        "好，有了這兩個獨立 Skill 後，接下來就是實戰見真章的時候了。"
        "Step 3：雙向開發與迭代。"
        "剛上線時，你一定會發現很多 edge case 報錯。比如：有些財務報銷因為員工寫得太口語，被分類成了『Other』；或者推薦的 assignee 居然是已離職的員工！沒關係，這就是『默會知識』暴露的過程。我們立刻回頭修改 SOP，補上最新在職員工庫匹配規則，以及財務關鍵字映射表。再次運行，分類準確度直接從 70% 飆升並穩定在 98% 以上！"
        "最後，Step 4：整合與安全防禦。"
        "我們用 Google Sheet MCP 和 Slack MCP 伺服器，把 triage 完的 JSON 數據自動寫入 Notion 的追蹤看板，並主動發送 Slack 動態通知給推薦的負責人，告訴他有新的 ticket進來了。"
        "同時，我們在最後加了一道人工安全 Checkpoint：當 category 為 Finance 且金額大於 $5000 元，或者是 IT 類別涉及管理權限變更時，Agent 會強制暫停，在管理員的 Slack 彈出確認視窗。只有管理員手動點擊 Approve，Agent 才會執行最後的寫入動作。"
        "透過這四步，一個原本每天耗費工程師好幾個小時、繁瑣無比的雜事分類流程，就這樣變成了一條每天在後台默默自動運作、出錯了你能在第一時間知道怎麼修、而且安全防禦 100% 點滿的 enterprise 級工作流了！"
    )
}

# Check variables
if API_KEY == "您的_ELEVENLABS_API_KEY_填在這裡" or VOICE_ID == "您的_CLONED_VOICE_ID_填在這裡":
    print("❌ 錯誤：請先將您的 ElevenLabs API Key 與 Voice ID 填入腳本的第 19 與 20 行！")
    sys.exit(1)

assets_dir = r"E:\Python檔案\GitHub research\AI agent research\assets"
os.makedirs(assets_dir, exist_ok=True)

print("🚀 正在連線至 ElevenLabs 雲端語音合成 API...")
print("🎙️ 正在使用您本人的 AI 克隆聲音為 Slide 4-9 頁批量生成高音質導讀語音...")

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

# API URL for multilingual synthesis (supports excellent Traditional Chinese)
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

for s_num, text in slides_text.items():
    print(f"\n📢 [Slide {s_num}] 正在發送合成請求 (字數: {len(text)} 字)...")
    
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2", # SOTA Chinese-supported model
        "voice_settings": {
            "stability": 0.55,           # 情感穩定度
            "similarity_boost": 0.85,    # 克隆音色相似度 (越高越接近本人)
            "style": 0.1,
            "use_speaker_boost": True
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            out_path = os.path.join(assets_dir, f"voice_slide_{s_num}.mp3")
            with open(out_path, "wb") as f:
                f.write(response.content)
            print(f"✅ 成功！音訊已儲存於：{out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")
        else:
            print(f"❌ 失敗：狀態碼 {response.status_code}，錯誤訊息：{response.text}")
    except Exception as e:
        print(f"❌ 發生異常：{e}")

print("\n🎉 所有 Slide 語音批量生成完畢！")
print("💡 提示：您現在可以直接在瀏覽器中開啟我們的簡報播放器。當檢測到本地有 voice_slide_X.mp3 時，網頁將自動無縫播放您專屬的克隆聲音進行完美口播！")
