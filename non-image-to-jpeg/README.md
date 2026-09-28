圖片處理器
這個 Python 腳本使用 Python Imaging Library（PIL）將圖像文件[".png", ".gif", ".bmp", ".tiff", ".webp", ".ico"] 
轉換為 JPEG 格式並刪除原始文件，並將JPEG 格式的文件放入原始位置。該腳本被設計成在指定的文件夾及其子目錄中遞歸搜索支援的圖像格式。

> ⚠️ **轉換後會刪除原始圖像檔案。請先備份。**

先決條件
Python 3.x
必需的 Python 套件：PIL、concurrent.futures、tqdm
用法
確保在您的系統上安裝了 Python 3.x。

安裝所需的套件：

pip install Pillow tqdm
把要轉換的圖像放置在指定的輸入文件夾中。

執行腳本：

python image_to_jpeg.py
配置
您可以通過修改腳本中的以下參數來配置腳本：

input_folder：指定腳本將搜索圖像文件的輸入文件夾。如果未提供，腳本將使用當前工作目錄。

supported_formats：在 supported_formats 列表中添加或刪除支援的圖像格式。

jpg_quality：設置轉換後圖像的 JPEG 品質（默認為 100）。

輸出
該腳本將每個圖像文件轉換為 JPEG 格式，並保存在原始文件所在的相同文件夾中。在轉換後，原始圖像文件將被刪除。

日誌
腳本使用日誌記錄警告和錯誤。您可以在控制台或配置的日誌文件中找到日誌。

注意事項
該腳本使用多進程方法（ProcessPoolExecutor）以提高轉換速度。

如果找不到文件或發生權限錯誤，腳本將記錄警告或錯誤。

在轉換和刪除過程完成後，按Enter鍵退出腳本。

請根據您的需求和偏好自由定制腳本。