import os
import shutil
#the file organiser using the oop
#create a class named file organiser
class  FileOrganiser:
    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.categories = {"Images":[".jpeg", ".jpg", ".png", ".gif", ".tiff", ".tif", ".bmp", ".svg", ".webp", ".heif", ".heic",
                         ".raw", ".avif", ".psd", ".eps", ".ico", ".ai", ".indd", ".pbm", ".pgm", ".ppm"],
                          "Documents":[".doc", ".docx", ".pdf", ".txt", ".rtf", ".xls", ".xlsx", ".csv", ".ppt", ".pptx",
                           ".odt", ".ods", ".odp", ".html", ".htm", ".xml", ".pages", ".md", ".markdown", ".epub", ".key"],
                           "Music":[".mp3", ".wav", ".aiff", ".flac", ".alac", ".aac", ".wma", ".ogg", ".m4a", ".dsd", ".pcm", ".opus"],
                           "Videos":[".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm", ".avchd", ".mpeg", ".mpg", ".3gp"],
                           }
        self.subfolder_paths = {}
#the organizer that create subfolders
    def create_subfolders(self):
        self.subfolder_paths ={"Images" :os.path.join(self.folder_path, "Images"),
                     "Documents": os.path.join(self.folder_path, "Documents"),
                     "Music": os.path.join(self.folder_path, "Music"),
                     "Videos": os.path.join(self.folder_path, "Videos"),
                     "Others": os.path.join(self.folder_path, "Others")}
        for path in self.subfolder_paths.values():
            os.makedirs(path,exist_ok= True)
    def organise_files(self):
        if len(os.listdir(self.folder_path)) == 0:
            print("oops! the folder is empty")
        for item in os.listdir(self.folder_path):
            item_path = os.path.join(self.folder_path,item)
            if not os.path.isfile(item_path):
             continue
            root,extension = os.path.splitext(item)
            extension = extension.lower()
            if extension in self.categories["Images"]:
                shutil.move(item_path,self.subfolder_paths["Images"])
            elif extension in self.categories["Documents"]:
                shutil.move(item_path, self.subfolder_paths["Documents"])
            elif extension in self.categories["Music"]:
                shutil.move(item_path, self.subfolder_paths["Music"])
            elif extension in self.categories["Videos"]:
                shutil.move(item_path, self.subfolder_paths["Videos"])
            else:
                shutil.move(item_path, self.subfolder_paths["Others"])
    def simulator(self):
        if len(os.listdir(self.folder_path)) == 0:
            print("oops! the folder is empty")
            return
        for item in os.listdir(self.folder_path):
            item_path = os.path.join(self.folder_path,item)
            if not os.path.isfile(item_path):
             continue
            root, extension = os.path.splitext(item)
            extension = extension.lower()
            if extension in self.categories["Images"]:
                print(f"{item} will go to----> Images/")
            elif extension in self.categories["Documents"]:
                print(f"{item} will go to----> Documents/")
            elif extension in self.categories["Music"]:
                print(f"{item} will go to----> Music/")
            elif extension in self.categories["Videos"]:
                print(f"{item} will go to----> Videos/")
            else:
                print(f"{item} will go to----> Others/")


print("welcome message")
folder_path = ""
while True:
    folder_pathS = input("enter the folder path \n>:")
    if not os.path.exists(folder_pathS):
        print("❌!folder does not exist❌")
    elif len(os.listdir(folder_pathS)) == 0:
        print("folder is  empty!🗑️🗑️")
    else:
        folder_path = folder_pathS
        break
while True:
    tidy = FileOrganiser(folder_path)
    menu = input("""what do want to do ?
                   1.organise a folder
                   2.Simulate (show what will happen)
                   3.Exit\n>""")
    if menu == "1":
        tidy.create_subfolders()
        tidy.organise_files()
        print("operation match with success✅")
    elif menu == "2":
        tidy.simulator()
    elif menu == "3":
        print("Exiting......")
        break








