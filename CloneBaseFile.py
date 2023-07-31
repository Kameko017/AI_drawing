import subprocess
import shutil
import os


repo_url = 'https://github.com/Kameko017/AI_drawing.git'
destination_path = '/content'
subprocess.run(['git', 'clone', repo_url, destination_path])


def check_file_exists(filename, search_path):
    for foldername, _, filenames in os.walk(search_path):
        for file in filenames:
            if file == filename:
                return os.path.join(foldername, file)
    return None


search_directory = '/content/drive/MyDrive/AI_drawing'

if not check_file_exists(filename='model_list.json',search_path=search_directory):
    source_file_path = '/content/AI_drawing/model_list.json'
    shutil.move(source_file, search_directory)

if not check_file_exists(filename='extension_list.json',search_path=search_directory):
    source_file_path = '/content/AI_drawing/extension_list.json'
    shutil.move(source_file, search_directory)


