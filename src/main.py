import os
import shutil

def main():
    copy_files_to_public()


def copy_files_to_public():
    if (os.path.exists("./static") != True):
        raise Exception("No static directory")
    
    shutil.rmtree("./public")
    os.mkdir("./public")

    copy_files()
    

def copy_files(current_directory="./static"):
    dir_content = os.listdir(current_directory)
    for item in dir_content:
        file_path = current_directory + "/" + item
        if os.path.isfile(file_path):
            new_location = file_path.replace("static", "public")
            shutil.copy(file_path, new_location)
        else:
            os.mkdir(file_path.replace("static", "public"))
            copy_files(file_path)

    
def list_files(current_directory="./static"):
    files = []
    dir_content = os.listdir(current_directory)
    for item in dir_content:
        file_path = current_directory + "/" + item
        if os.path.isfile(file_path):
            files.append(file_path)
        else:
            files.extend(list_files(file_path))

    return files

main()