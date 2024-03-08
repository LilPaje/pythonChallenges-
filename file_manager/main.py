import os
import platform
import sys
from pathlib import Path
import time

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
    filepath = f'C:/Users/{user}/{folder}/teste'
    dir_file_list = os.listdir(filepath)
    print(dir_file_list)
    for i in dir_file_list:
        print(i)
        os.remove(filepath+f"/{i}")

def windows_remove_files_from_folder(user):
    list_folders = ["Documents", "Images", "Downloads"]
    print("Which folder do you want to exclude the files?")
    print("[1] Documents")
    print("[2] Images")
    print("[3] Downloads")
    print("[0] Cancel")

    input_user = str(input("-> "))
    if input_user == "0":
        time.sleep(2.5)
        print("Canceling...")
        main()

    elif input_user == "1" or input_user == "2" or input_user == "3":
        print("Removing...")
        remove_files(user,list_folders[int(input_user)-1])
        time.sleep(2.5)
        main()

    else:
        print("Invalid value, please try again")
        time.sleep(2.5)
        main()
    

def main():
    welcome() 
    print("Select the option: ")
    print("[1] Clear folder")
    print("[2] Change Files Location")
    print("[0] Exit")
    if platform.system() == 'Windows':
        windows_remove_files_from_folder(os.getlogin())

main()

#get_number_of_users_windows()