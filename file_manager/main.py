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

def remove_files(user):
    folder = choose_folder()
    if folder == '-1':
        pass
    else:
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


def choose_folder():
    list_folders = ["Documents", "Images", "Downloads"]
    print("Which folder do you want to exclude the files?")
    print("[1] Documents")
    print("[2] Images")
    print("[3] Downloads")
    print("[0] Cancel")

    input_user = str(input("-> "))
    if input_user == "0":
        print("Canceling")
        return "-1"
    elif input_user == "1" or input_user == "2" or input_user == "3":
        return list_folders[int(input_user)-1]
    
    else:
        print("Invalid value, please try again")
        choose_folder()

def create_folder(path):
    print("This type of file don't have a folder in your system, do you want to create one?Y/n")
    create_a_folder = input(str("-> "))
    if create_a_folder == "Y" or create_a_folder == "y":
        os.mkdir(path)
        return True

    elif create_a_folder == "N" or create_a_folder == "n":
        return False

    else: 
        print("Invalid entry, please try again.")
        time.sleep(2.5)
        create_folder()

    
        

def organize_files(user):
    #list_extensions = [".pdf",".exe",".msi",".jpg",".png",".jif",".txt"]
    

    input_user = choose_folder()
    if input_user == "-1":
        pass
    else: 
        path = f'C:/Users/{user}/{input_user}'
        list_itens_on_folder = os.listdir(path)
        if "Organizing Files" not in os.listdir(f'C:/Users/{user}/Documents/'):
            os.mkdir(f'C:/Users/{user}/Documents/Organizing Files/')
        list_itens_destiny_folder = os.listdir(f'C:/Users/{user}/Documents/Organizing Files/')
        print("Organizing")
        for j in list_itens_on_folder:
            if j[-3:] in list_itens_destiny_folder:
                shutil.move(path+'/'+j,f'C:/Users/{user}/Documents/Organizing Files/'+j[-3:])
                #print(j[-4:])
                print(list_itens_destiny_folder)
            else:
                new_folder = create_folder(f'C:/Users/{user}/Documents/Organizing Files/'+j[-3:])
                if new_folder == True:
                    shutil.move(path+'/'+j,f'C:/Users/{user}/Documents/Organizing Files/'+j[-3:])
                    list_itens_destiny_folder.append(j[-3:])
                else: 
                    if "other" not in os.listdir(f'C:/Users/{user}/Documents/Organizing Files'):
                        os.mkdir(f'C:/Users/{user}/Documents/Organizing Files/other')
        
                    shutil.move(path+'/'+j,f'C:/Users/{user}/Documents/Organizing Files/other/')
            

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
            remove_files(os.getlogin())
            time.sleep(2.5)
            main()
    elif input_user == '2':
        organize_files(os.getlogin())
        main()

    else:
        print("Invalid value, please try again")
        time.sleep(2.5)
        main()


main()

#get_number_of_users_windows()