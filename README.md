# tools

一些自己寫的小工具腳本。都很小，各自獨立，沒有套件管理，也沒有 CI。

原本各自是三個獨立 repo，這裡合併在一起方便維護。

> ## ⚠️ 兩個轉換工具會「刪除原始檔案」
>
> `wav-to-mp3` 與 `non-image-to-jpeg` 在轉換成功後**會刪除原始檔案**。
> 這是原本的設計，合併時未修改。
>
> **執行前請先備份。** 這兩個工具不會問你第二次。

## 工具列表

| 工具 | 說明 | 依賴 |
|---|---|---|
| [`wav-to-mp3/`](wav-to-mp3/) | 批次把資料夾（含子資料夾）內的 `.wav` 轉成 `.mp3`，然後**刪除原始 `.wav`** | `tqdm`, `ffmpeg-python`, 系統需有 `ffmpeg` |
| [`non-image-to-jpeg/`](non-image-to-jpeg/) | 遞迴把 `.png` `.gif` `.bmp` `.tiff` `.webp` `.ico` 轉成 `.jpg`，然後**刪除原始檔** | `Pillow`, `tqdm` |
| [`flatten-folders/`](flatten-folders/) | 把「只有一個子資料夾」的父資料夾，子資料夾的內容往上移一層，刪除空的子資料夾 | 無（標準函式庫） |

## 執行

```bash
pip install tqdm ffmpeg-python Pillow
```

三個工具都是單一檔案腳本，直接執行即可。用法細節見各自的 README。

```bash
# 在 wav-to-mp3/ 目錄下
python wav_to_mp3.py
python wav_to_mp3.py --bitrate 192k --sample_rate 44100
```

## 關於 `wav-to-mp3` 的執行檔

原本的 repo 裡有打包好的 `dist/convert.exe`（約 8.4 MB 的 PyInstaller 產物）。
**這個二進位檔沒有帶過來**，因為編譯產物不該進版控。

需要執行檔的話自行打包：

```bash
pip install pyinstaller
pyinstaller --onefile wav_to_mp3.py
```

產物會在 `dist/wav_to_mp3.exe`（已被 `.gitignore` 排除）。

## 合併時做了哪些更動

為了讓這些腳本在合併後可用，只做了以下**表面**變更，**程式邏輯完全未動**：

| 變更 | 原因 |
|---|---|
| `1.py` → `wav_to_mp3.py` | 檔名 `1.py` 無法辨識用途 |
| `1.py` → `image_to_jpeg.py` | 同上 |
| `README-Chinese.md` → `README.zh-TW.md` | 統一語系檔名格式 |
| 每個工具移到自己的子資料夾 | 讓三個工具可以共存 |
| 移除 `dist/convert.exe` | 編譯產物不應進版控 |
| 新增根目錄 `.gitignore` | 排除 build 產物與 Python 快取 |

每個工具的原始碼內容與原本 repo **逐行相同**。原本三個 repo 的 commit 都是
「修改說明文字」這類的文件微調，沒有保留價值，因此合併為單一 commit。

## 授權

MIT，見根目錄的 [`LICENSE`](LICENSE)。
