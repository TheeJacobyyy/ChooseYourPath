import streamlit as st
import os

if 'player_name' not in st.session_state:
    st.session_state.player_name = None

if 'current_scene' not in st.session_state:
    st.session_state.current_scene = 'start'

if 'weapon' not in st.session_state:
    st.session_state.weapon = None

if st.session_state.player_name is None:
    st.write("Welcome to 'Choose Your Path!'")
    player_name = st.text_input("What is your name?", key="name_input")

    if player_name:
        st.session_state.player_name = player_name
        st.text("Choose your weapon:")
        weapon_choice = st.selectbox("Pick a weapon", ["Sword", "Axe"])

        if weapon_choice:
            st.session_state.weapon = weapon_choice

        st.success(f"Nice to meet you, {player_name}! Let's start our journey!")
        if st.button("Start Game"):
            st.session_state.current_scene = 'start'
            st.rerun
else:
    story = {

        "start": {
            "text": f"Welcome, {st.session_state.player_name}. We start at the crossroads of our journey. Will you take the left path or the right path?",
            "choices": {
                "Left": "left",
                "Right": "right"
            }
        },
        "left": {
            "text": "You went left and found a dark forest. There are multiple paths and seems to be eerie.",
            "choices": {
                "Right": "left_right_path",
                "Straight": "left_straight_path",
                "Left": "left_left_path"
            }
        },
        "right": {
            "text": "You go right and walk for some time. You find an old trader. Will you try to barter or mug him?",
            "choices": {
                "Barter": "right_path_barter",
                "Mug": "right_path_mug", 
            }
        },
        "right_path_barter": {
            "text": "You attempt to barter, lets see if your kindliness is respected...",
            "choices": {}
        },
        "right_path_mug": {
            "text": "You chose not to waste time, lets see how well your weapon holds up in combat...",
            "choices": {}
        }
    }

    current_scene = st.session_state.current_scene
    st.write(story[current_scene]["text"])

    if current_scene == "right_path_barter":
        if st.session_state.weapon == "Sword":
            st.write("He was a magic man! He took advantage of your kind and used his magic and turned you into a frog.")
            st.write("Game Over")
        elif st.session_state.weapon == "Axe":
            st.write("You chopped his head off and found a pouch of magic beans.")
            st.write("Will you continue on your path or reveal the power of the beans?")
            if st.button("PLant Beans"):
                st.session_state.current_scene = "axe_barter"
                st.rerun

    elif current_scene == "right_path_mug":
        if st.session_state.weapon == "Sword":
            st.write("He zapped you with his wand and collected your soul.")
            st.write("Game Over.")
        elif st.session_state.weapon == "Axe":
            st.write("You decapitated him with your mighty axe and stole his pouch of magic beans.")
    
    else:
        for choice, next_scene in story[current_scene]["choices"].items():
            if st.button(choice):
                st.session_state.current_scene = next_scene

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://th.bing.com/th/id/R.c1554d4740dbad096ce7c931fccaf339?rik=k7C3AY7OvjzDQQ&riu=http%3a%2f%2fpixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com%2fimage%2f9f71130ad1ab517.png&ehk=Sdd9U27XJSaFGH0tWEM4mUspLvoBjzxQ2omsTagukCU%3d&risl=&pid=ImgRaw&r=0");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)


# def clear_screen():
#     os.system("cls" if os.name == "nt" else "clear")

# def start_game():
#     name = input("Hello wanderer, what is your name?: ")
#     clear_screen()
#     print("Hello " + name + " welcome to my quest.")

#     #Should We Continue
#     should_we_play = input("Are you up for the challenge? (yes/no) ").lower()

#     if should_we_play == "y" or should_we_play == "yes":
#         clear_screen()
#         print("We shall start!")
#         weapon = input("Choose your weapon (sword/axe): ").lower()
#         clear_screen()
        
#     #First Choice
#         direction = input("Do you want to go left or right? (left/right) ").lower()
#         clear_screen()

#         if direction == "left":
#             print("You went left and found a dark forest. There are multiple paths and seems to be eerie.")
#             #Second Choice of Left
#             choose_path_left(weapon)

#         elif direction == "right":
#             action = input("You go right and walk for some time. You find an old trader. Will you try to barter or mug him?  (barter/mug) ").lower()
#             clear_screen()

#             if action == "barter":
#                 if weapon == "sword":
#                     print("He took advantage of your kind and used his magic and turned you into a frog.")
#                     print("Game Over.")
#                     return
                
#                 elif weapon == "axe":
#                     print("You chopped his head off and found a pouch of magic beans.")
#                     action = input("Do you plant the beans or continue on your path? (plant/continue) ").lower()
#                     clear_screen()

#                     if action == "plant":
#                         print("A giant bean stalk has grown thru the clouds.")
#                         action = input("Do you climb the stalk or chop it down with your mighty axe? (climb/chop)").lower()
#                         clear_screen()

#                         if action == "climb":
#                             print("You attempted to brave the stalk by climbing it.")
#                             print("You fell to your death.")
#                             print("Game Over.")
#                             return
                        
#                         elif action == "plant":
#                             print("You chopped the stalk down and it crushed you as it fell.")
#                             print("Game Over.")
#                             return
                        
#                     elif action == "continue":
#                         print("You continued on your path for many more miles only to die of dehydration.")
#                         print("Game Over.")
#                         return

#             elif action == "mug":
#                 if weapon == "sword":
#                     print("He zapped you with his wand and collected your soul.")
#                     print("Game Over.")
#                     return
                
#                 elif weapon == "axe":
#                     action = input("You decapitated him with your mighty axe and stole his pouch of magic beans. Do you plant them or continue on the path? (plant/continue)").lower()
#                     clear_screen()

#                     if action == "plant":
#                         print("A mighty bean stalk taller than the heavens has grown.")
#                         action = input("Will you climb or chop it down? (climb/chop)").lower()
#                         clear_screen()

#                         if action == "climb":
#                             print("You attempted to climb the mighty stalk and fell to your death.")
#                             print("Game Over.")
#                             return
                        
#                         elif action == "chop":
#                             print("You chopped down the mighty stalk and it rained gold coins from the heavens down, making you abundantly rich.")
#                             print("You Won!")
#                             return
                        
#                     elif action == "continue":
#                         print("You continued down the path and found nothing.")
#                         print("Now you are hungry and died of starvation.")
#                         print("Game Over.")
#                         return

#     else:
#         clear_screen()
#         print("We are NOT playing...")

# def choose_path_left(weapon):
#     while True:
#         path_choice = input("You see three paths ahead of you. Straight, right and left. Which direction will you go? (straight/right/left)").lower()
        
#         clear_screen()

#         #Left Action Choice
#         if path_choice == "left":
#             action = input("You go left and see a giant hedge. Should we try to climb it? (yes/no)").lower()
#             clear_screen()

#             if action == "yes":
#                 print("You attempted to climb the hedge. It was too tell and you fell down.")
#             elif action == "no":
#                 print("The hedge does look intimidating, maybe we should save our strength.")
#         #Straight Action Choice

#         elif path_choice == "straight":
#             action = input("You've went straight. There is a river flowing heavily downstream. Will you attempt to brave the waters? (yes/no)").lower()
#             clear_screen()

#             if action == "yes":
#                 print("You attempted to brave the waters and drowned from the currents.")
#                 print("Game Over.")
#                 return
            
#             elif action == "no":
#                 print("This seems to be a good choice. We shall live to see another day!")

#         #Right Path Choice
#         elif path_choice == "right":
#             action = input("You went right. There seems to be an open path with nothing in the distance. Keep walking? (yes/no)").lower()
#             clear_screen()

#             #THIS IS WHERE YOU LEFT OFF. FIGURE OUT HOW TO RETURN TO OPEN PATH IF THEY DONT ENTER THE CAVE. IF THEY RETURN AND CONTINUE DIE OF DEHYDRATION
#             if action == "yes":
#                 print("You continued walking and stumbled upon a cave.")
#                 action = input("Do you want to enter the cave? (yes/no)").lower()
#                 clear_screen()

#                 #IM PRETTY SURE YOU TAKE THIS MAKE A FUNCTION LIKE THE MAIN CHOICE PATH AND MAKE A NEW RETURN CHOICE IF NOT "no."
#                 if action == "yes":
#                     print("The cave is warm and you hear sounds of heavy breathing.")
#                     action = input("Investigate the noises or return? (investigate/return)").lower()
#                     clear_screen()

#                     if action == "investigate":
#                         action = input("You found a dragon and a pile of gold he is protecting. The dragon fly's toward you. Will you fight or retreat? (fight/retreat)").lower()
#                         clear_screen()

#                         if action == "fight":
#                             if weapon == "sword":
#                                 print("You drew your sword courageously, slew the dragon and claimed his pile of gold for your own.")
#                                 print("You Won.")
#                                 return
                            
#                             elif weapon == "axe":
#                                 print("Your axe was no match for the dragon. He burnt you into smithereens.")
#                                 print("Game Over")
#                                 return
                            
#                         elif action == "retreat":
#                             print("You retreated like a cowardly dog.")
#                             print("You exited the cave and continue on your path walking for hours only to find nothing and die of dehydration...")
#                             print("Game Over.")
                            
#                     elif action == "return":
#                         print("You returned to your comfortable path, taking no risks. Your reward was you walked for miles to find nothing and die of dehydration...")
#                         print("Game Over.")
#                         return
                        
#                 elif action == "no":
#                     print("You continue on your path walking for hours only to find nothing and die of dehydration...")
#                     print("Game Over.")
#                     return

#             elif action == "no":
#                 print("Turn back to the three paths.")

#         return_choice = input("Do you want to return to the three previous paths or keep wallowing over your choice?: (yes/no)").lower()
#         clear_screen()

#         if return_choice == "yes":
#             print("You are back at the three paths.")
#             continue
#         elif return_choice == "no":
#             print("Continue to wallow then coward. Return when you develop some courage.")
#             break

# if __name__ == "__main__":
#     start_game()