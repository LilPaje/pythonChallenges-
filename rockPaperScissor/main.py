#We will ask the user to select either rock paper or scissors. And we will also make the
# computer choose one out of three randomly. Now we will check who won the game and give
# them a score. This is done 5 times to say who has won finally and we will ask the user
# if they want to continue or reset and continue or exit the game.
import random
import time


def pc_choice_for_rock_paper_scissor():
    rock_paper_scissor_list = ["r", "p", "s"]
    return rock_paper_scissor_list[random.randint(0,2)]

def player_choice_for_rock_paper_scissor(num):
    rock_paper_scissor_list = ["r", "p", "s"]
    return rock_paper_scissor_list[num]

def game(user_input):
    pc_choice = pc_choice_for_rock_paper_scissor()
    print(f"Pc's Choice: {pc_choice}")
    player_choice = player_choice_for_rock_paper_scissor(user_input)
    if(pc_choice == player_choice):
        return "Draw"
    elif(pc_choice == "r" and player_choice == "s"):
        return "pc"
    elif(pc_choice == "p" and player_choice == "r"):
        return "pc"
    elif(pc_choice == "s" and player_choice == "p"):
        return "pc"
    elif (player_choice == "r" and pc_choice == "s"):
        return "player"
    elif (player_choice == "p" and pc_choice == "r"):
        return "player"
    else:
        return "player"

def welcome(pc_wins, player_wins):
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
    print(f"Player score: {player_wins}")
    print(f"Pc score: {pc_wins}")
    
def main(pc_wins, player_wins):
    welcome(pc_wins,player_wins)

    print("Select your option:")
    print("[1] For Rock")
    print("[2] For Paper")
    print("[3] For Scissor")
    print("[0] To stop playing")

    input_user = str(input("\n-> "))
    
    if (input_user == "0"):
        print("Finishing the game... See Ya :D")

    elif(input_user == "1" or input_user == "2" or input_user == "3"):
        game_result = game(int(input_user))
        
        if game_result == "Draw":
            print(f"{game_result}")
            time.sleep(2.5)
            main(pc_wins, player_wins)

        elif game_result == "pc":
            print("Pc Wins!")
            time.sleep(2.5)
            main(pc_wins+1, player_wins)

        else: 
            print("Player Wins!")
            time.sleep(2.5)
            main(pc_wins, player_wins+1)

            


    else:
        print("Invalid Number, try again!")
        time.sleep(2.5)
        main(pc_wins, player_wins)

    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(0,0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
