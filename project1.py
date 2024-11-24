import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def start_game():
    name = input("Hello wanderer, what is your name?: ")
    clear_screen()
    print("Hello " + name + " welcome to my quest.")

    #Should We Continue
    should_we_play = input("Are you up for the challenge? (yes/no) ").lower()

    if should_we_play == "y" or should_we_play == "yes":
        clear_screen()
        print("We shall start!")
        weapon = input("Choose your weapon (sword/axe): ").lower()
        clear_screen()
        
    #First Choice
        direction = input("Do you want to go left or right? (left/right) ").lower()
        clear_screen()

        if direction == "left":
            print("You went left and found a dark forest. There are multiple paths and seems to be eerie.")
            #Second Choice of Left
            choose_path_left(weapon)

        elif direction == "right":
            choice = input("Okay, you now see a bridge, do you want to swim under or cross it? (swim/cross) ").lower()
            clear_screen()
            if choice == "swim" and weapon == "axe":
                print("You got eaten by a brain eating amoeba.")
                print("Game Over.")
            else:
                print("You successfully crossed and banged Princess Peach!")

    else:
        clear_screen()
        print("We are NOT playing...")

def choose_path_left(weapon):
    while True:
        path_choice = input("You see three paths ahead of you. Straight, right and left. Which direction will you go? (straight/right/left)").lower()
        
        clear_screen()

        #Left Action Choice
        if path_choice == "left":
            action = input("You go left and see a giant hedge. Should we try to climb it? (yes/no)").lower()
            clear_screen()

            if action == "yes":
                print("You attempted to climb the hedge. It was too tell and you fell down.")
            elif action == "no":
                print("The hedge does look intimidating, maybe we should save our strength.")
        #Straight Action Choice
        elif path_choice == "straight":
            action = input("You've went straight. There is a river flowing heavily downstream. Will you attempt to brave the waters? (yes/no)").lower()
            clear_screen()

            if action == "yes":
                print("You attempted to brave the waters and drowned from the currents.")
                print("Game Over.")
                return
            elif action == "no":
                print("This seems to be a good choice. We shall live to see another day!")
        #Right Path Choice
        elif path_choice == "right":
            action = input("You went right. There seems to be an open path with nothing in the distance. Keep walking? (yes/no)").lower()
            clear_screen()
            #THIS IS WHERE YOU LEFT OFF. FIGURE OUT HOW TO RETURN TO OPEN PATH IF THEY DONT ENTER THE CAVE. IF THEY RETURN AND CONTINUE DIE OF DEHYDRATION
            if action == "yes":
                print("You continued walking and stumbled upon a cave.")
                action = input("Do you want to enter the cave? (yes/no)").lower()
                clear_screen()

                if action == "yes":
                    print("The cave is warm and you hear sounds of heavy breathing.")
                    action = input("Investigate the noises or return? (investigate/return)").lower()
                    clear_screen()

                    if action == "investigate":
                        action = input("You found a dragon and a pile of gold he is protecting. The dragon fly's toward you. Will you fight or retreat? (fight/retreat)").lower()
                        clear_screen()

                        if action == "fight":
                            if weapon == "sword":
                                print("You drew your sword courageously, slew the dragon and claimed his pile of gold for your own.")
                                print("You Won.")
                                return
                            elif weapon == "axe":
                                print("Your axe was no match for the dragon. He burnt you into smithereens.")
                                print("Game Over")
                                return
                            
                        elif action == "retreat":
                            print("You retreated like a cowardly dog.")
                            
                    elif action == "return":
                        print("You returned to your comfortable path, taking no risks.")
                elif action == "no":
                    print("You continue on your path.")

            elif action == "no":
                print("Turn back to the three paths.")

        return_choice = input("Do you want to return to the three previous paths or keep wallowing over your choice?: (yes/no)").lower()
        clear_screen()

        if return_choice == "yes":
            print("You are back at the three paths.")
            continue
        elif return_choice == "no":
            print("Continue to wallow then coward. Return when you develop some courage.")
            break

if __name__ == "__main__":
    start_game()