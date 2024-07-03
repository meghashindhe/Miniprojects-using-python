import os
import shutil
file_types = { 'images':['.jpeg', '.jpg', '.png','.gif', '.bmp'], 'documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],'videos': ['.mp4', '.avi', '.mov', '.mkv'], 'music' : ['.mp3', '.wav', '.aac']}

def list_of_files(directory):
    for entry in os.scandir(directory):
        if entry .is_file():
            yield entry.name

def create_directories(directory, categories):
    for category in categories:
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def move_files(directory, files, file_types):
    for file in files:
        file_path = os.path.join(directory, file)
        file_ext = os.path.splitext(file)[1].lower()
        moved = False
        for category, extensions in file_types.items():
            if file_ext in extensions:
                dest_dir = os.path.join(directory, category)
                shutil.move(file_path, os.path.join(dest_dir, file))
                moved = True
                break
        if not moved:
            others_dir = os.path.join(directory, 'others')
            if not os.path.exists(others_dir):
                os.makedirs(others_dir)
            shutil.move(file_path, os.path.join(others_dir, file))

def organize_files(directory):
    files = list_of_files(directory)
    create_directories(directory, file_types.keys())
    move_files(directory, files, file_types)

target_directory = 'D:\Downloads'
organize_files(target_directory)
