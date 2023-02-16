import shutil
import os

def getDeleteFolder(folderPath):
    path = os.path.join(folderPath,"running")

    folder_path = path
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"{folder_path} and its contents have been deleted.")
        except OSError as e:
            print(f"Error: {folder_path} and its contents could not be deleted - {e}")
    else:
        print(f"{folder_path} does not exist.")
