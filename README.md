# 《台北動漫散步指南》Taipei Anime Walk

> 一本帶著個人品味、同好黑話、體感溫度與文化記憶的**「台北二次元線上風格獨立誌（Webzine）兼散步地圖」**。

[![Deploy to GitHub Pages](https://github.com/JohnsonChung/taipei-anime-walk/actions/workflows/deploy.yml/badge.svg)](https://github.com/JohnsonChung/taipei-anime-walk/actions/workflows/deploy.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 📖 專案願景與核心哲學

這不是冰冷的商業黃頁或大拜拜五星評分庫，而是專為漫遊者打造的台北二次元空間誌：

1. **個人風格大於中庸評分**：擁抱主觀觀點，記錄通道寬窄、紙箱油墨氣味、防吃土背包禮儀與老店神物出沒處。
2. **動線大於散落點位**：嚴格落實「一筆畫散步原則」，量化體力消耗（1~5 ⚡）與背包會車指數，提供明確的中繼回血「歇腳錨點」。
3. **記憶大於即時刪除**：老店拉下鐵捲門絕不直接抹去，而是蓋上「時光膠囊」印章，沉澱為台北二次元地景演進史。
4. **完全無商用與零成本**：全站無廣告、無業配。基於純靜態 SSG 架構與免費開源圖資，零伺服器維護負擔。

---

## 🤖 模組化 AI 深度介入指引體系 (AI Guidelines)

專案將 AI 角色明確約束為「編輯室後勤秘書」，依生命週期拆分為 5 份獨立指引：

| 模組指引 | 角色定位 | 核心職責與邊界 |
| :--- | :--- | :--- |
| [`01-editorial-curator.md`](guidelines/ai/01-editorial-curator.md) | **編輯室主觀風格專員** | 嚴格禁絕 AI 罐頭廢話，刻劃感官細節，補全避坑提醒與歇腳錨點。 |
| [`02-spatial-navigator.md`](guidelines/ai/02-spatial-navigator.md) | **空間拓撲與動線專員** | 一筆畫動線驗證、體力消耗條（1~5 星）與背包友善指數評估。 |
| [`03-data-cleanser.md`](guidelines/ai/03-data-cleanser.md) | **圖資清洗與 Schema 專員** | 解析 Google My Maps KML，去蕪存菁，自動劃入商圈聚落並對齊 Zod。 |
| [`04-community-archivist.md`](guidelines/ai/04-community-archivist.md) | **社群轉譯與時光膠囊專員** | 將 Issue 投稿轉為規範 PR，撰寫歇業名店文化印記。 |
| [`05-tech-guardian.md`](guidelines/ai/05-tech-guardian.md) | **純靜態架構守門專員** | 嚴禁伺服器後端、嚴禁付費圖資 API，守護 GitHub Pages 零成本架構。 |

---

## 🛠️ 技術架構 (Technology Stack)

* **靜態網站生成器**：[Astro 5](https://astro.build/)（零 JS 優先、Markdown Content Collections、Zod Schema 嚴格型別安全）
* **樣式與獨立誌排版**：[Tailwind CSS](https://tailwindcss.com/)（日系暖白紙質調、微顆粒紋理、時光膠囊印章）
* **地圖渲染引擎**：[Leaflet.js](https://leafletjs.com/) + **CARTO Positron** 極簡淺灰日系底圖（完全免 API Key、零帳單風險）
* **資料庫與儲存**：純 Git 倉庫託管之 Markdown/GeoJSON 檔案
* **自動化構建發布**：GitHub Actions ➔ GitHub Pages

---

## 🚀 本地開發指南 (Quickstart)

```bash
# 1. 複製專案庫
git clone https://github.com/JohnsonChung/taipei-anime-walk.git
cd taipei-anime-walk

# 2. 安裝相依套件
npm install

# 3. 啟動本地開發預覽 (支援熱重載)
npm run dev

# 4. 靜態編譯建置
npm run build

# 5. 本地預覽編譯後產物
npm run preview
```

### 圖資解析工具
若手邊有從 Google My Maps 匯出之 `raw_map.kml` 或 `raw_map.kmz`：
```bash
python scripts/parse_kml_seed.py scripts/seeds/raw_map.kml
```

---

## 📮 社群共筆與投稿沙龍

本專案以 **GitHub 作為唯一的同好沙龍與品味過濾器**：
- **推薦新點位**：點擊專案上方 `Issues` ➔ 選擇 `[新點位投稿]`，填寫空間體感與避坑細節。
- **歇業名店通報**：選擇 `[時光膠囊封存]`，留下它曾帶給你的時代回憶。
- **程式碼與路線修訂**：直接提交 Pull Request，CI 將自動進行 Frontmatter 格式校驗。

---

## 📜 授權協議 (License)

* 內容與路線資料：[創用 CC 姓名標示-非商業性 4.0 國際 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)
* 程式碼部分：MIT License
