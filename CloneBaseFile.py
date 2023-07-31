import shutil
import os

def check_file_exists(filename, search_path):
    for foldername, _, filenames in os.walk(search_path):
        for file in filenames:
            if file == filename:
                return os.path.join(foldername, file)
    return None

def check_folder_exists(foldername, search_path):
    for folder in os.listdir(search_path):
        if os.path.isdir(os.path.join(search_path, folder)) and folder == foldername:
            return os.path.join(search_path, folder)
    return None

search_directory = '/content/drive/MyDrive/AI_drawing'
if check_folder_exists("AI_drawing","/content/drive/MyDrive/"):
    os.makedirs(search_directory)
    print('make AI_drawing file')

if not check_file_exists(filename='model_list.json',search_path=search_directory):
    source_file = '/content/AI_drawing/model_list.json'
    shutil.copy(source_file, search_directory)

if not check_file_exists(filename='extension_list.json',search_path=search_directory):
    source_file = '/content/AI_drawing/extension_list.json'
    shutil.copy(source_file, search_directory)


