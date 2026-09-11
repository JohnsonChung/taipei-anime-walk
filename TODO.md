# 專案待辦與未來功能清單 (TODO.md)

本文件記錄《台北動漫散步指南》暫緩或未來預計擴充的功能規劃與技術評估。

---

## 📌 待辦功能一：個人 Google My Maps 與網站雙向冷同步系統 (Cold Sync)

### 1. 需求描述
- 在站長指定維護時間（On-Demand），將個人的 Google My Maps 與網站資料庫進行雙向地點冷同步。
- 支援手機外出時在 Google Maps 打點後一鍵拉取更新到網站，也支援網站新增的社群投稿地點一鍵導出回推至個人 My Maps。

---

### 2. 技術架構與雙向工作流評估

| 同步方向 | 自動化程度 | 技術機制與實作方式 |
| :--- | :---: | :--- |
| **Google My Maps ➔ 本網站 (Inbound Pull)** | **100% 全自動** | 透過 My Maps 免金鑰 KML 端點 (`https://www.google.com/maps/d/kml?mid=<MID>&forcekml=1`) 下載解析，自動比對 `src/content/spots/`。<br/>- **新地點**：自動生成對應商圈的 Markdown 骨架。<br/>- **座標微調**：更新 frontmatter `coordinates`，**絕不覆蓋既有的散文與漫遊提醒**。 |
| **本網站 ➔ Google My Maps (Outbound Export)** | **半自動 (5 秒)** | 因 Google 官方未開放 My Maps 直接寫入 API（標記為 Infeasible），網站提供一鍵導出指令生成標準 `taipei_anime_walk.kml`，於 My Maps 介面點選「重新匯入並替換所有項目」，即可一鍵刷新個人地圖。 |

---

### 3. 預計實作步驟
1. 建立獨立同步腳本 `scripts/sync-mymaps.mjs`。
2. 在 `package.json` 加入 CLI 指令：
   - `"sync:pull": "node scripts/sync-mymaps.mjs pull"`
   - `"sync:export": "node scripts/sync-mymaps.mjs export"`
3. 設定環境變數 `GOOGLE_MYMAPS_MID`。
4. 導入差異檢測報告 (Diff Table)，在終端機列出「My Maps 新增 / 網站新增 / 座標微調」之比對項目。

---

## 📌 待辦功能二：散步路線瀏覽人氣與熱門度統計系統

### 1. 需求描述
- 在「散步路線」獨立分頁 (`/walks`) 及路線詳細頁中，顯示各路線的瀏覽人氣與熱度指標。
- 讓漫遊者能一目了然哪幾條路線最受歡迎（例如加上「🔥 最多人走過」熱門標籤）。
- 提供依「🔥 人氣熱門 / ⚡ 步調輕鬆 / 預設精選」排序路線的功能。
- 支援讀者互動（例如「❤️ 想去這條路線」或「👣 走過打卡」）。

---

### 2. 靜態網站 (GitHub Pages / SSG) 技術評估與候選方案

| 方案 | 優點 | 限制與注意事項 | 推薦度 |
| :--- | :--- | :--- | :---: |
| **方案 A：雙軌制 (基準底數 + 客戶端 LocalStorage 累加)** | 零伺服器成本、免註冊任何第三方帳號、不受瀏覽器 Adblock 阻擋、初次載入不尷尬（有底數） | 瀏覽數與足跡僅保存在讀者本地瀏覽器，無法實現跨讀者全域即時大數據同步 | ⭐⭐⭐⭐ (推薦第一階段) |
| **方案 B：Cloudflare Workers + KV** | 免費額度充足、極速邊緣響應、完全掌控 API 與隱私 | 需設定 Cloudflare 帳號與部署 Worker 腳本 | ⭐⭐⭐⭐ (推薦長期全域同步) |
| **方案 C：Supabase / Firebase Serverless** | 具備完整資料庫、可擴充讀者留言與真實打卡照片 | 需維護後端專案密鑰，靜態頁面前端需呼叫外部 SDK | ⭐⭐⭐ |
| **方案 D：第三方開源計數器 (如 GoatCounter / Waline)** | 專為靜態網站設計、開箱即用 | 容易被部分嚴格的瀏覽器隱私外掛或阻擋器（uBlock Origin）攔截導致數字歸零 | ⭐⭐ |

---

### 3. 未來實作切入步驟
1. 確定跨訪客數據同步策略（採方案 A 本地互動，或方案 B Cloudflare KV 全域計數）。
2. 在 `src/components/WalkCard.astro` 中加入熱度徽章與排序資料屬性 (`data-views`, `data-stamina`)。
3. 在 `src/pages/walks/index.astro` 提供「人氣最高 / 步調輕鬆」即時重排邏輯。
4. 在路線詳細頁 `src/pages/walks/[...slug].astro` 觸發瀏覽記錄增加。
