BLUE = "\033[94m"
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
#DUPLICATION
import os
import shutil
#create a class named fileorganiser
class  FileOrganiser:
#init method that take self.categories
    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.categories = {"Images":[".jpeg", ".jpg", ".png", ".gif", ".tiff", ".tif", ".bmp", ".svg", ".webp", ".heif", ".heic",
                         ".raw", ".avif", ".psd", ".eps", ".ico", ".ai", ".indd", ".pbm", ".pgm", ".ppm"],
                          "Documents":[".doc", ".docx", ".pdf", ".txt", ".rtf", ".xls", ".xlsx", ".csv", ".ppt", ".pptx",
                           ".odt", ".ods", ".odp", ".html", ".htm", ".xml", ".pages", ".md", ".markdown", ".epub", ".key"],
                           "Music":[".mp3", ".wav", ".aiff", ".flac", ".alac", ".aac", ".wma", ".ogg", ".m4a", ".dsd", ".pcm", ".opus"],
                           "Videos":[".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm", ".avchd", ".mpeg", ".mpg", ".3gp"],
                           }
#create important functions
#create subfolders functions that have a dictionary of paths
    def create_subfolders(self):
        self.paths = {"Images": os.path.join(self.folder_path,"Images"),
                 "Documents":os.path.join(self.folder_path,"Documents"),
                 "Music": os.path.join(self.folder_path,"Music",),
                 "Videos": os.path.join(self.folder_path,"Videos"),
                 "Others": os.path.join(self.folder_path,"Others")
                 }
#check if our folder only content subfolders or files or both of them
        for item in  os.listdir(self.folder_path):
            item_path = os.path.join(self.folder_path,item)
# dont create subfolders if it content only subfolders
            if os.path.isdir(item_path):
                continue
            else:
                for path in self.paths.values():
# dont forget exist_ok = True when create subfolders
                    os.makedirs(path,exist_ok= True)
#define the get extension function that return thr category of file
    def get_extensions(self,item_extension):
        _, extension = os.path.splitext(item_extension)
        extension = extension.lower()
        for category,extension_list in self.categories.items():
            if extension in extension_list:
                return category
        return "Others"
#define the organizer that ignore the folders and move only subfolders
    def organiser(self):#folder_case
        files = []
        status = False
        for item in os.listdir(self.folder_path):
            item_path = os.path.join(self.folder_path,item)
#check the status that the folder content only subfolders
            if os.path.isfile(item_path):
                files.append(item)
                category = self.get_extensions(item)
                shutil.move(item_path,self.paths[category])
                status = True
            elif os.path.isdir(item_path):
                continue
        if len(files)==0:
            print(YELLOW+"the folder contain only subfolders!"+RESET)
            status = False
        if status == True:
            print(GREEN+"operation matched with success"+RESET)
#define simulation function thats also be careful in the case that we have only subfolders
    def simulator(self):
        files = []
        for item in os.listdir(self.folder_path):
            item_path = os.path.join(self.folder_path, item)
            # check the status that the folder content only subfolders
            if os.path.isfile(item_path):
                files.append(item)
                category = self.get_extensions(item)
                print(f"{item} will moved to----> {category}/")
            if os.path.isdir(item_path):
                continue
        if len(files) == 0:
            print(YELLOW+"the folder contain only subfolders"+RESET)
#start a while loop that check the folder status
folder_path = ""
while True:
    folder = input("enter the folder you wanna organize it\n>:")
    if not os.path.exists(folder):
        print(RED+"the folder does not exist"+RESET)
    elif len(os.listdir(folder)) == 0:
        print(YELLOW+"the folder is empty"+RESET)
    else:
        folder_path = folder
        break
#create the main while loop that give the menu and check the choices
print("👋welcome to the file organiser🤗")
while True:
    tidy = FileOrganiser(folder_path)
    menu = input("""
====================================
          FileOrganiser
====================================
1.Organise a folder📁
2.simulation (show what will happen)👀
3.Exit🚪
--------------------------------------
chose an option(1-3)\n>:""")
    if menu == "1":
        tidy.create_subfolders()
        tidy.organiser()
    elif menu == "2":
        print("-"*20+f"{BLUE}simulation mode👀{RESET}"+ 20 *"-")
        tidy.simulator()
        print("-" * 57)
    elif menu == "3":
        confirm_option = input(f"do want to {RED}Exit{RESET}?(y/n)\n>:")
        if confirm_option.lower() == "y":
            print(RED+"Exiting......"+RESET)
            break
        else:
            continue
    else:
        continue