import os
import shutil

def flatten_folders(root_folder):
    # 获取根文件夹中的所有子文件夹
    subfolders = [folder for folder in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, folder))]
    
    for folder_name in subfolders:
        folder_path = os.path.join(root_folder, folder_name)
        sub_subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]
        
        if len(sub_subfolders) == 1:
            sub_subfolder_name = sub_subfolders[0]
            sub_subfolder_path = os.path.join(folder_path, sub_subfolder_name)
            
            # 获取子文件夹内的所有内容
            sub_subfolder_contents = [os.path.join(sub_subfolder_path, item) for item in os.listdir(sub_subfolder_path)]
            
            # 将子文件夹内的内容移动到父文件夹
            for item_path in sub_subfolder_contents:
                new_item_path = os.path.join(folder_path, os.path.basename(item_path))
                shutil.move(item_path, new_item_path)
            
            # 删除子文件夹
            shutil.rmtree(sub_subfolder_path)

# 获取脚本所在路径
script_folder = os.path.dirname(os.path.abspath(__file__))

# 调用函数处理脚本所在路径下的文件夹
flatten_folders(script_folder)
