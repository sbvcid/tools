# Convert WAV to MP3

This tool simplifies the process of converting multiple WAV files, both in the current folder and its subfolders, to MP3 format.

- **Source Code:** `wav_to_mp3.py`

> ⚠️ **Original `.wav` files are deleted after a successful conversion. Back up first.**

## How to Use

1. **Install Dependencies:**
    Make sure the required dependencies are installed, and that `ffmpeg` is available on your system:
    ```bash
    pip install tqdm ffmpeg-python
    ```

2. **Run the Program:**
    ```Shell
    python wav_to_mp3.py
    ```

3. **Conversion Process:**
    - The program scans the current and subfolders for `.wav` files.
    - Converts them to `.mp3`, placing the new files in the same folder.
    - Original `.wav` files are deleted.

4. **Completion:**
    - After completion, the terminal will display "All files converted and deleted."
    - Press Ctrl+C to interrupt if needed.

## Custom Settings

- Customize bitrate and sample_rate during runtime.
    - `bitrate`: Specify MP3 bitrate (default: "320k").
    - `sample_rate`: Specify MP3 sample rate (default: "48000").
    - Example: `python wav_to_mp3.py --bitrate 192k --sample_rate 44100`

## Optional: build a standalone executable

The packaged `convert.exe` from the original repository is not included here, since
build artifacts do not belong in version control. To build it yourself:

```bash
pip install pyinstaller
pyinstaller --onefile wav_to_mp3.py
```

The result is written to `dist/wav_to_mp3.exe` (which is git-ignored).
