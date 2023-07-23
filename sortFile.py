import os
import sys
from shutil import move
arrList = os.listdir()
path = os.getcwd()
# newPath = '\py\Downloads\Organized'+'\Organized'

extensions = {
    ".zip": "ZipFile",
    ".pdf": "Documents",
    ".mp3": "Audio",
    ".jpg": "Images",
    ".jpeg": "Pictures",
    ".docx": "Word",
    ".py": "Python",
    ".js": "Javascript",
    ".html": "HTML",
    ".mp4": "Videos",
    ".mkv": "Videos"
}

for key in extensions:
    for file in arrList:
        file_path = os.path.join(path, file)
        newPath = os.path.join(path, extensions[key])

        # To Find the current working script/file name
        script_file_name = os.path.basename(sys.argv[0])
        # This condition is to filter the working file/script from moving/creating the directory
        if (file != script_file_name):
            if (file.endswith(key)):
                if not os.path.exists(newPath):
                    os.mkdir(newPath)
            # directory = os.mkdir(newPath)
            # destination = os.path.join(newPath, extensions[key])
            # # destination = os.path.join(newPath, extensions[key])
                print('-'*50)
                print("File '%s' moved Sucessfully to '%s' Directory." %
                      (file, extensions[key]))
                print('-'*50)
                move(file_path, newPath)
