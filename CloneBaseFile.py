import shutil

search_directory = '/content/drive/MyDrive/AI_drawing'

if not check_file_exists(filename='model_list.json',search_path=search_directory):
    source_file_path = '/content/AI_drawing/model_list.json'
    shutil.move(source_file, search_directory)

if not check_file_exists(filename='extension_list.json',search_path=search_directory):
    source_file_path = '/content/AI_drawing/extension_list.json'
    shutil.move(source_file, search_directory)


