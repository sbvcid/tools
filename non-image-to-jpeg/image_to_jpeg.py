from PIL import Image
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageProcessor:
    def __init__(self, input_folder=None):
        self.input_folder = input_folder or os.path.abspath(".")

    def find_image_files(self):
        image_files = []
        supported_formats = [".png", ".gif", ".bmp", ".tiff", ".webp", ".ico"]  # 添加支援的格式
        for root, dirs, files in os.walk(self.input_folder):
            for file in files:
                if any(file.lower().endswith(format) for format in supported_formats):
                    image_files.append(os.path.join(root, file))
        return image_files

    def convert_and_delete_image(self, input_path, output_folder, jpg_quality=95):
        try:
            filename, ext = os.path.splitext(os.path.basename(input_path))
            output_path = os.path.join(os.path.dirname(input_path), f"{filename}.jpg")  # 使用原始圖片文件的相同子資料夾

            # 打開圖像
            img = Image.open(input_path)

            # 將圖像保存為 JPG 格式，設置品質為 100
            img.convert("RGB").save(output_path, "JPEG", quality=jpg_quality)

            os.remove(input_path)

            return f"轉換 {filename} 完成，並刪除原始圖片檔案"
        except FileNotFoundError:
            logging.warning(f"文件 {input_path} 未找到")
        except PermissionError as e:
            logging.error(f"PermissionError: {e}")

def process_images():
    current_folder = os.path.abspath(".")
    output_folder = current_folder

    image_processor = ImageProcessor()
    image_files = image_processor.find_image_files()
    total_files = len(image_files)

    if total_files == 0:
        print("未找到任何圖片文件.")
        return

    print(f"Found {total_files} image files to process.")

    progress = 0

    with ProcessPoolExecutor() as executor, tqdm(total=total_files) as pbar:
        futures = [executor.submit(image_processor.convert_and_delete_image, file, output_folder) for file in image_files]
        for future in as_completed(futures):
            result = future.result()
            progress += 1
            pbar.update(1)
            pbar.set_description(f"處理進度：{progress}/{total_files} ({(progress / total_files) * 100:.2f}%) - {result}")

    print("\n所有檔案轉換和刪除完成")

if __name__ == "__main__":
    process_images()
    print("Press Enter to exit...")
    input()
