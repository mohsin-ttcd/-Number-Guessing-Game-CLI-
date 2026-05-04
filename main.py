#import random module
import random

# Number guessing game inside a function
def play_number_guessing_game():

    target_number = random.randint(0,20)
    max_guess_limit = 5
    attempt = 1 
    win = 0
    lose = 0
    play = 1

    print(f"\n***** Game Start *****")
    print(f"*** Max guess limit {max_guess_limit} ***")
    print(f"Enter number between 0 - 20\n")

    while max_guess_limit > 0:

        # Count remaining attempt
        attempt_left = max_guess_limit - 1
                
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
            print(f"🎮 You enter: {user_input}")
            print(f"👆 You have tried {attempt} times.\n")
            win = 1
            break
        
        elif user_input > target_number:
            print(f"\n❌ Too high!")
            print(f"🔄️ Try again! Remaining attempt {attempt_left}.\n")

        else:
            print("\n❌ Too low!")
            print(f"🔄️ Try again! Remaining attempt {attempt_left}.\n")

        max_guess_limit = max_guess_limit - 1
        attempt = attempt + 1
        
    # Game over check
    if max_guess_limit == 0:
        print("\n❌ Game Over!")
        print("❌ You hit the max limit!")
        print(f"🎯 Target number was {target_number}\n")
        lose = 1

    return win, lose, play

total_win = 0
total_lose = 0
game_play = 0

# Main loop 
# Run the game
while True:

    win, lose, play = play_number_guessing_game()
    total_win += win
    total_lose += lose
    game_play += play


    while True:

        replay = input(f"Do you want to play again? y/n: ").lower()

        if replay == "y" or replay == "n":
            break
        else:
            print(f"\n❌ Invalid input! Please enter 'y' for yes and 'n' for no.")

    
    if replay == "n":
        print(f"\n🥳 Game End!\n")
        print(f"▶️ You played {game_play} round.")
        print(f"🏆 Won {total_win} & 😔 Lost {total_lose}.")
        break
        
    else:
        continue


# New feature to add 
# tracking the fewest number of attempts it took to win