import os
import shutil

# ベースフォルダの第一階層のみZIP化
def zip_folders(base_folder):
    subfolders = [f.path for f in os.scandir(base_folder) if f.is_dir()]
    for folder_path in subfolders:
        zip_filename = f"{folder_path}.zip"
        shutil.make_archive(folder_path, 'zip', folder_path)
        # shutil.rmtree(folder_path)

# ベースのフォルダを指定
base_folder = r'E:\imagezip_tmp'
zip_folders(base_folder)
