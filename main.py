# number guessing game

#import random module
import random

#wrape number guessing game inside a function
def play_number_guessing_game():

    #target and max guess limit
    target_number = random.randint(0,20)
    max_guess_limit = 5


    print(f"***** Game Start *****")
    print(f"*** Max guess limit {max_guess_limit} ***")
    print(f"Enter number between 0 - 20\n")

    while max_guess_limit > 0:

        # Input validation
        try:
            user_input = int(input("Guess The Number: "))
        
        except ValueError:
            print("\n❌ Please enter a integer number between 0 - 20\n")
            continue


        # Game engine logic
        if user_input == target_number:
            print(f"\n🥇 You won the game!")
            print(f"🎯 Target number was {target_number}")
            print(f"🎮 You enter: {user_input}\n")
            break
        
        elif user_input > target_number:
            print(f"\n❌ Too high!")
            print("🔄️ Try again!\n")

        else:
            print("\n❌ Too low!")
            print("🔄️ Try again!\n")

        max_guess_limit = max_guess_limit - 1

    # Game over check
    if max_guess_limit == 0:
        print("\n❌ Game Over!")
        print("❌ You hit the max limit!\n")
        print(f"🎯 Target number was {target_number}")


# Main loop 
# Run the game
while True:
    play_number_guessing_game()

    replay = input(f"Do you want to play again? y/n: ").lower()

    if replay == "n":
        print(f"\n🥳 Game End!\n")
        break
        
    else:
        continue
