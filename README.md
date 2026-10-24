# 歐洲近期示威與暴動事件熱區地圖 (European Unrest & Riot Heatmap)

互動式歐洲近期示威與暴動熱區監測地圖（涵蓋 17 大熱區、21 座核心城市），支援 **Google Maps JavaScript API**（Vector Map、`AdvancedMarkerElement`、`Circle` 熱區、`Polyline` 跨國擴散軌跡）與**內建無段縮放向量熱力地圖**雙引擎切換。

## 功能特色

- **雙地圖引擎無縫切換**：
  - **Google Maps 向量地圖**：載入 `GOOGLE_MAPS_API_KEY` 後自動啟用 Google Maps JavaScript API (`v=weekly`)，支援流暢縮放、街景服務（Street View）與全螢幕檢視。
  - **內建無段縮放熱區圖**：免金鑰即可直接使用滑鼠滾輪縮放（1.0x – 8.0x）、拖曳平移與熱力半徑動態調整。
- **17 大歐洲示威與暴動熱區情資**：
  - 包含事件導火線、衝突過程、政府維安與宵禁應對措施，以及每起事件的新聞與官方警示來源連結。
- **議題與風險等級篩選**：
  - 依「教育與青年風暴」、「居住正義與高房價」、「通膨與反緊縮」、「反貪腐與民主憲政」、「移民與庇護衝突」及風險等級（Level 3–5）即時篩選。

## 快速啟動

1. 複製環境變數範本並填入您的 `GOOGLE_MAPS_API_KEY`（不會被 Git 追蹤）：
   ```bash
   cp .env.example .env
   ```
   於 `.env`（或 `api_key.txt`）填入：
   ```env
   GOOGLE_MAPS_API_KEY=您的_API_KEY
   ```

2. 啟動本地端伺服器（會自動讀取 `.env` 並注入前端，且不將金鑰寫入原始碼）：
   ```bash
   python3 server.py
   ```

3. 開啟瀏覽器前往：
   ```
   http://localhost:8080
   ```
