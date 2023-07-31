import shutil
import os
import subprocess

def check_file_exists(filename, search_path):
    for foldername, _, filenames in os.walk(search_path):
        for file in filenames:
            if file == filename:
                return os.path.join(foldername, file)
    return None

search_directory = '/content/drive/MyDrive/AI_drawing'
if not os.path.exists(search_directory):
    os.makedirs(search_directory)

if not check_file_exists(filename='model_list.json',search_path=search_directory):
    source_file = '/content/AI_drawing/model_list.json'
    shutil.copy(source_file, search_directory)

if not check_file_exists(filename='extension_list.json',search_path=search_directory):
    source_file = '/content/AI_drawing/extension_list.json'
    shutil.copy(source_file, search_directory)


subprocess.run(['git', 'clone','-b', 'v2.4','https://github.com/camenduru/stable-diffusion-webui' ,'/content/camenduru'])