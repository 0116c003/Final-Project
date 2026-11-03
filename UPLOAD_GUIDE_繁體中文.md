# GitHub 上傳方式（Proposal ③+④）

**③ GitHub Repository**：上傳整個 `DietSense_GitHub_Starter` 資料夾中的檔案與子資料夾到已建立的 GitHub Repository。

**④ DESIGN.md**：已放在專案根目錄，老師可直接在 GitHub 首頁點選。設計圖在 `docs/architecture/`。

## 方法 A：GitHub 網頁上傳
1. 打開你已建立的 GitHub repository。
2. 選 `Add file` → `Upload files`。
3. **將壓縮檔解壓縮後的「內部檔案及資料夾」拖曳進去**，不要直接上傳 ZIP 作為專案內容，也避免多出一層資料夾。
4. Commit message 輸入：`Initial DietSense proposal design and prototype`，按 `Commit changes`。
5. 確認首頁看得到 `README.md`、`DESIGN.md`、`src/`、`docs/`。

## 方法 B：Windows CMD + Git
```cmd
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```
把解壓縮後**內部全部檔案**複製到上述專案資料夾，再執行：
```cmd
git add .
git commit -m "Initial DietSense proposal design and prototype"
git push origin HEAD
```

## 本機測試
在專案根目錄 CMD 執行：
```cmd
python -m unittest discover -s tests -v
python -m src.dietsense.cli --food demo_rice --grams 150
```

## 注意
- README 是 GitHub 首頁專題介紹；DESIGN.md 是老師要的持續維護文件。
- 目前只有可運作的基本熱量/BMR/TDEE 計算；LLM、RAG、資料庫串接仍屬計畫。
- 不要上傳真實 API Key、個人飲食紀錄或其他個資。
- Proposal 的 Word/PPT 已一起附上，若 GitHub 預設公開，請確認文件沒有姓名、學號或敏感資訊後再公開。
