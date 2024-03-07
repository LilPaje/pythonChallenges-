#We will ask the user to select either rock paper or scissors. And we will also make the
# computer choose one out of three randomly. Now we will check who won the game and give
# them a score. This is done 5 times to say who has won finally and we will ask the user
# if they want to continue or reset and continue or exit the game.
import random


def pc_choice_for_rock_paper_scissor():
    rock_paper_scissor_list = ["r", "p", "s"]
    return rock_paper_scissor_list[random.randint(0,2)]

def player_choice_for_rock_paper_scissor(num):
    rock_paper_scissor_list = ["r", "p", "s"]
    return rock_paper_scissor_list[num]

def game(user_input):
    pc_choice = pc_choice_for_rock_paper_scissor(user_input)
    player_choice = player_choice_for_rock_paper_scissor()
    if(pc_choice == player_choice):
        return "Draw"
    elif(pc_choice == "r" and player_choice == "s"):
        return "pc"
    elif(pc_choice == "p" and player_choice == "r"):
        return "pc"
    elif(pc_choice == "s" and player_choice == "p"):
        return "pc"
    elif (player_choice == "r" and pc_choice == "s"):
        return "pc"
    elif (player_choice == "p" and pc_choice == "r"):
        return "pc"
    else:
        return "pc"

def welcome():
    print("""
╭━━━╮╱╱╱╱╱╭╮╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱┃┃╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
┃╰━╯┣━━┳━━┫┃╭╮┃╰━╯┣━━┳━━┳━━┳━╮┃╰━━┳━━┳┳━━┳━━┳━━┳━╮
┃╭╮╭┫╭╮┃╭━┫╰╯╯┃╭━━┫╭╮┃╭╮┃┃━┫╭╯╰━━╮┃╭━╋┫━━┫━━┫╭╮┃╭╯
┃┃┃╰┫╰╯┃╰━┫╭╮╮┃┃╱╱┃╭╮┃╰╯┃┃━┫┃╱┃╰━╯┃╰━┫┣━━┣━━┃╰╯┃┃
╰╯╰━┻━━┻━━┻╯╰╯╰╯╱╱╰╯╰┫╭━┻━━┻╯╱╰━━━┻━━┻┻━━┻━━┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯""")

    print("\n---Welcome to Rock Paper em Scissor---")
    
def main():
    welcome()


    select


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
