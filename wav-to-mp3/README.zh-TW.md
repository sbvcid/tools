# 把 WAV 轉換成 MP3 (Convert WAV to MP3)

這個小工具可以幫助你將當前資料夾中，以及子資料夾的所有 WAV 檔案批量轉換為 MP3 格式。

原始碼是 `wav_to_mp3.py`。

> ⚠️ **轉換成功後會刪除原始的 `.wav` 檔案。請先備份。**

## 如何使用

1. **安裝依賴庫 ffmpeg-python：**
    請確保你已經安裝了必要的依賴庫，並且系統上有 `ffmpeg`，你可以使用以下指令進行安裝：
   ```bash
   pip install tqdm ffmpeg-python
   ```
2. 執行腳本：
    ```Shell
    python wav_to_mp3.py
    ```
3. 等待轉換：程式將遍歷當前資料夾中，以及子資料夾的 .wav 檔案，將它們轉換成 .mp3 檔案，放在在相同的資料夾中，並刪除原始的 .wav 檔案。
4. 程式運行完成後，終端機會顯示 "所有檔案轉換和刪除完成"。若中途想停止，按下Ctrl+C可以中斷。


## 自定義設定

您可以在執行時通過命令行參數自定義 bitrate、sample_rate。例如：

```Shell
python wav_to_mp3.py --bitrate 192k --sample_rate 44100
```

bitrate：指定 MP3 的位元率，預設為 "320k"。
sample_rate：指定 MP3 的取樣率，預設為 "48000"。

## 選用：打包成獨立執行檔

原本 repo 裡打包好的 `convert.exe` 沒有帶過來，因為編譯產物不該進版控。
需要的話可以自行打包：

```bash
pip install pyinstaller
pyinstaller --onefile wav_to_mp3.py
```

產物會在 `dist/wav_to_mp3.exe`（已被 `.gitignore` 排除）。

