import random
import time

# Global state 
braindmg = False
chance = False

def start_game():
    print("\n-------HOTEL ADVENTURE-------")
    time.sleep(2)
    print("\nInstructions: When choosing between the choices, choose the corresponding number. When prompted with a yes/no question, type only yes or no. Typing anything else wont work ")
    input("Press Enter to start...")
    print("\n-------------Floor 3---------------")
    time.sleep(2)
    print("You wake up in a dark, cold hotel room ")
    time.sleep(2)
    print("You dont remember youself going to sleep in here. Yet here you are.")
    time.sleep(3)
    print("Can you escape out safely?")
    time.sleep(2)
    input("Press Enter to go outside the room...")
    floor3_hallway()

def floor3_hallway():
    print("You are in a dark hallway. It is eerily quiet.")
    time.sleep(3)
    print("You walk ahead. You can hear your own heartbeat")
    time.sleep(3)
    print("\nYou reach a point. You see 3 ways to go to.")
    time.sleep(3)
    print("\n1. A creepy door, swinging to and fro on its own")
    time.sleep(3)
    print("2. Take the Elevator directly to the ground floor")
    time.sleep(3)
    print("3. Take the staircases to Floor 2")
    time.sleep(2)
    print("Choose wisely")
    time.sleep(2)
    choice=input(">")
    if choice=="1":
        creepy_door()
    elif choice=="2":
        elevator()
    elif choice=="3":
        staircase_f2() # Added ()
    else:
        print("Invalid choice. Try again. The monsters are watching...")
        time.sleep(3)
        floor3_hallway()

def creepy_door():
    print("\nYou chose the creepy door. Inside, a giant red button floats")
    time.sleep(3)
    print("On the button, it says 'DO NOT PRESS'. Should you press it?")
    time.sleep(3)
    choice=input("Press it? (yes/no):")
    if choice.lower().strip()=="yes":
        time.sleep(2)
        print("\nBOOM! You're back in your house. You won. It was all a dream...or was it?")
        print("\n-------------YOU WON---------------")
    else:
        print("\nYou hesitate. The door slam shuts behind you.")
        time.sleep(2)
        print("The Window opens, and something invisible pulls you outside")
        time.sleep(3)
        print("\nYou fall to death. You lost")
        print("\n-------------YOU DIED---------------")

def elevator():
    print("\nYou step into the Elevator. Uh oh! the cables snap.")
    time.sleep(2)
    print("You plummet to 3 floors the ground. Will you survive?")
    time.sleep(3)
    print("You did not make it. You are dead. You Lost")
    print("\n-------------YOU DIED---------------")

def staircase_f2():
    print("\nYou walk down the creaky wooden stairs")
    time.sleep(3)
    floor2_hallway() # Added call to move the game forward

def floor2_hallway():
    print("\n-------------Floor 2---------------")
    time.sleep(2)
    print("\nThe air is thicker here. You see 2 doors")
    time.sleep(2)
    print("1. A door with a bright red 'DANGER' sign.")
    time.sleep(3)
    print("2. A storage room with strange noises coming from inside.")
    time.sleep(3)
    print("Choose wisely")
    choice=input("> ").strip()
    if choice=="1":
        danger_room()
    elif choice=="2":
        storage_room()

def danger_room():
    print("\nIt is pitch black. You cannot see anything")
    global braindmg
    if braindmg:
        print("Your head is throbbing. Your legs move without permission!")
        time.sleep(3)
        move=random.choice(["forward","back"]).lower().strip()
        print("You stumbled ",move)
        time.sleep(2)
    else:
        move=input("Do you want to move forward or back?")
        time.sleep(2)
    
    if move.lower()=="forward":
        time.sleep(2)
        print("\nAAAAAARGH!!! You fall down a extremely deep pit.")
        time.sleep(3)
        print("\n-------------YOU DIED---------------")
        time.sleep(3)
    else:
        print("You walk back to the hallway to safety.")
        time.sleep(2)
        print("Who knows what was in there?")
        time.sleep(2)
        floor1_hallway()

def storage_room():
    global braindmg
    print("You enter the store room. You see furniture flying everywhere")
    time.sleep(2)
    print("A wooden chair flies across the room and SMASHES into your head.")
    braindmg=True
    time.sleep(3)
    print("Everything is spinning. You feel dizzy")
    time.sleep(2)
    print("You stumble out of the room and walk down the staircases to Floor 1")
    time.sleep(4)
    floor1_hallway()

def floor1_hallway():
    print("\n-------------Floor 1---------------")
    time.sleep(3)
    print("You are now at Floor 1. This floor is darker than Floor 2")
    time.sleep(3)
    print("You see the Electrical Room and the staircases that lead to the Ground floor. What do you choose?")
    time.sleep(4)
    print("1. Enter the humming Electrical Room")
    time.sleep(2)
    print("2. Continue down to the Ground Floor")
    time.sleep(2)
    choice=input("> ").strip()
    if choice=="1":
        electrical_room()
    elif choice=="2":
        ground_floor_lobby()
    else:
        print("Invalid Choice! Try Again. The monsters are watching!")
        floor1_hallway()

def electrical_room():
    # Calling the puzzle and checking result
    if electrical_puzzle():
        pass # The 'WON' logic is now inside the puzzle function
    else:
        print("\n-------------YOU DIED---------------")
        time.sleep(3)

def electrical_puzzle():
    print("\n-------------ELECTRICAL SYSTEM OVERRIDE---------------")
    print("I have chosen a number between 1 and 100.")
    time.sleep(2)
    print("You have a total of 10 attempts to restore power. Can you guess it?")
    time.sleep(3)
    
    num = random.randint(1, 100)
    guess = 0 
    attempt = 10
    
    while guess != num and attempt > 0:
        try:
            print(f"\nYou have {attempt} attempts remaining")
            guess = int(input("Enter your guess: "))
            attempt -= 1
            
            if guess < num:
                print("Too low! The voltage is dropping...")
            elif guess > num:
                print("Too high! The system is overloading...")
            else:
                print(f"BINGO! The number was {num}. Power Restored!")
                time.sleep(3)
                print("You see a door open. You run towards it and teleport to your bed")
                print("\n-------------YOU WON---------------")
                return True
        except ValueError:
            print("\nPlease enter a valid whole number")
            
    print(f"\nGame Over! You were electrocuted. The number was {num}")
    return False

def ground_floor_lobby():
    print("\n-------------GROUND FLOOR---------------")
    time.sleep(3)
    print("This is the Ground Floor. The exit must be close.")
    time.sleep(3)
    print("You see 3 ways to proceed forward")
    time.sleep(2)
    print("1. Enter the Indoor Playground")
    time.sleep(2)
    print("2. Enter the Cafeteria")
    time.sleep(2)
    print("3. Enter the Staff Room")
    time.sleep(2)
    print("Choose Wisely")
    time.sleep(1)
    choice=input("> ").strip()
    if choice=="1":
        playground_room()
    elif choice=="2":
        cafeteria()
    elif choice=="3":
        staff_room()
    else:
        print("The exit is so close. Don't give up now!")
        time.sleep(1)
        ground_floor_lobby()

def playground_room():
    global chance
    print("\nYou enter the playground room")
    time.sleep(2)
    print("Bright plastic slides and ball pits fill the room")
    time.sleep(3)
    print("You see a giant TV screen showing a live feed of the room")
    time.sleep(3)
    print("In the TV, a monster is standing right behind you. You panic and look back")
    time.sleep(3)
    print("You see nothing. You feel a sense of relief. You turn back to the TV")
    time.sleep(3)
    print("\nAAAAAAAAAARGH WHAT IS THAT")
    time.sleep(2)
    print("YOU SEE A GIANT MONSTER INFRONT OF YOU. IT IS SO TALL THAT ITS FACE ISN'T VISIBLE.")
    time.sleep(4)
    if chance:
        print("\n-------------SECOND CHANCE ACTIVATED---------------")
        print("The monster lunges, but your Golden Ticket glows white, blinding it!")
        time.sleep(3)
        print("You scramble back to the lobby")
        chance=False
        time.sleep(3)
        ground_floor_lobby()
    else:
        print("\nThe Monster crushes you under its big feet")
        time.sleep(3)
        print("\n-------------YOU DIED---------------")

def cafeteria():
    global chance 
    print("\nYou enter the cafeteria")
    time.sleep(2)
    print("Rows of empty tables stretch into the dark")
    time.sleep(3)
    print("You see a glowing piece of paper that says 'Golden Ticket'.")
    time.sleep(3)
    take=input("Do you take the ticket?[yes/no]").lower().strip()
    if take=="yes":
        chance=True
        print("You feel a strange warmth. You now have a second chance to save you from the next bad decision")
        time.sleep(4)
    else:
        print("You leave it. Maybe you dont believe in luck.")
        time.sleep(2)
    print("You walk back out in the lobby")
    time.sleep(2)
    ground_floor_lobby()

def staff_room():
    print("You are now in the staff room.")
    time.sleep(2)
    print("A strange man in a suit is sitting at a desk, staring at the wall")
    time.sleep(3)
    print("1. Talk to him")
    time.sleep(2)
    print("2. Ignore him and turn away")
    time.sleep(2)
    choice=input("> ").strip()
    if choice=="1":
        print("\nThe man smiles.")
        time.sleep(2)
        print("Man:I've been waiting for you")
        print("He opens a portal")
        time.sleep(2)
        print("Man: This is way out")
        print("You trust him, hold you breath and...")
        time.sleep(3)
        print("You jump into the portal")
        time.sleep(3)
        print("\nBANG! YOU ARE BACK HOME")
        time.sleep(3)
        print("\n-------------YOU WON---------------")
    else:
        print("\nYou turn around and try to run away.")
        time.sleep(3)
        print("\nBut then...")
        time.sleep(3)
        print("\nYou hear a cry behind you")
        time.sleep(2)
        print("The man feels betrayed. He was waiting there for so long to save you, but you betrayed him. He is in tears")
        time.sleep(5)
        print("Man: YOU ARE A FILTHY BETRAYER. I SHOULD'VE NEVER WAITED FOR YOU HERE. YOU DESERVE TO DIE")
        time.sleep(5)
        print("The man runs up to you and stabs you to death")
        time.sleep(3)
        print("\n-------------YOU DIED---------------")

while True:
    start_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
input("Press ENTER to exit")

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.