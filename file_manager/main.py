import os
import platform
#import sys
from pathlib import Path
import time
import shutil

def welcome():
    
    print("""
╭━━━╮╭╮╱╱╱╱╭━╮╭━╮
┃╭━━╯┃┃╱╱╱╱┃┃╰╯┃┃
┃╰━━┳┫┃╭━━╮┃╭╮╭╮┣━━┳━╮╭━━┳━━┳━━┳━╮
┃╭━━╋┫┃┃┃━┫┃┃┃┃┃┃╭╮┃╭╮┫╭╮┃╭╮┃┃━┫╭╯
┃┃╱╱┃┃╰┫┃━┫┃┃┃┃┃┃╭╮┃┃┃┃╭╮┃╰╯┃┃━┫┃
╰╯╱╱╰┻━┻━━╯╰╯╰╯╰┻╯╰┻╯╰┻╯╰┻━╮┣━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
          """)

#def get_number_of_users_windows():
#    os.system('net user > users.txt')
#    users = Path('./users.txt').read_text()
#    print(users)

def remove_files(user, folder):
    filepath = f'C:/Users/{user}/{folder}'
    dir_file_list = os.listdir(filepath)
    for i in dir_file_list:
        print(i, end=", ")

    print("\nThe files above will be permanently excluded. Do you want to proceed?Y/n")
    input_user = str(input("->"))
    if input_user == 'Y' or 'y':
        for i in dir_file_list:
            #print(filepath+f"/{i}")
            if os.path.isfile(filepath+f"/{i}"):
                os.remove(filepath+f"/{i}")
                #print(os.path.isdir(filepath+f"/{i}"))
            else: 
                shutil.rmtree(filepath+f"/{i}")

    elif input_user == 'N' or 'n':
        print("Canceling...")
        time.sleep(2.5)
    else:
        print("Invalid Number, please try again")
        remove_files(user,folder)


def windows_remove_files_from_folder(user):
    list_folders = ["Documents", "Images", "Downloads/teste"]
    print("Which folder do you want to exclude the files?")
    print("[1] Documents")
    print("[2] Images")
    print("[3] Downloads")
    print("[0] Cancel")

    input_user = str(input("-> "))
    if input_user == "0":
        print("Canceling...")
    elif input_user == "1" or input_user == "2" or input_user == "3":
        print("Removing...")
        remove_files(user,list_folders[int(input_user)-1])
    else:
        print("Invalid value, please try again")


def organize_files(path):
    list_extensions = [".pdf",".exe",".msi",".jpg",".png",".jif"]
    list_itens_on_folder

def main():
    welcome() 
    print("Select the option: ")
    print("[1] Clear folder")
    print("[2] Organize Files")
    print("[0] Exit")

    input_user = str(input("-> "))
    if input_user == "0":
        print("Exiting the code")

    elif input_user == '1':
        if platform.system() == 'Windows':
            windows_remove_files_from_folder(os.getlogin())
            time.sleep(2.5)
            main()
    elif input_user == '2':
        pass

    else:
        print("Invalid value, please try again")
        time.sleep(2.5)
        main()


main()

#get_number_of_users_windows()