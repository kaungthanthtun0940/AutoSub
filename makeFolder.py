import os

def getMakeFolder(folderPath):
        path1 = folderPath
        path2 = "running"

        full_path = os.path.join(path1, path2)
        print(full_path)
        try:
            os.makedirs(full_path)

        except OSError:
            print("Creation of the directory %s failed" % full_path)
        else:
            print("Successfully created the directory %s " % full_path)


