#import random module
import random


# choose a range (1–50, 1–100) function.
def difficulty_level(lower_bound):

    print(f"\n***** Welcome to the Custom Number Guessing Game! *****\n")
    print(f"⚓ Choose your difficulty level!")
    print(f"🔈 Max guess limit up to 7 and lower bound will be {lower_bound}.\n")

    # Take input and validate it
    while True:

        try:
            target_between = int(input(f"Enter the highest number you want to guess up to (eg: 50, 100, 500):... "))

            if target_between >= lower_bound:
                break
            else:
                print(f"\n❌ {target_between} is less than {lower_bound}.")
                print(f"🔈 Please enter an integer number greater than {lower_bound}.\n")

        except ValueError:
            print(f"\n ❌ Invalid input, Please enter an integer number greater than {lower_bound}.\n")
            continue

    print(f"\n✅ Awesome! Setting up a game from 0 to {target_between}.\n")

    return target_between
# Number guessing game inside a function
def play_number_guessing_game(max_guess_limit, target_between):

    target_number = random.randint(0,target_between)
    attempt = 1 
    win = 0
    lose = 0
    play = 1

    print(f"\n***** Game Start *****")
    print(f"*** Max guess limit {max_guess_limit} ***")
    print(f"Enter number between 0 - {target_between}\n")

    while max_guess_limit > 0:

        # Count remaining attempt
        attempt_left = max_guess_limit - 1
        
        # Input validation
        try:
            user_input = int(input("Guess The Number: "))
        
        except ValueError:
            print(f"\n❌ Please enter a integer number between 0 - {target_between}\n")
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

    return win, lose, play, attempt

lower_bound = 50
max_guess_limit = 7
total_win = 0
total_lose = 0
game_play = 0
best_score = []

# Let the player choose a range (1–50, 1–100)
target_between = difficulty_level(lower_bound)

# Main loop 
# Run the game
while True:
    win, lose, play, attempt= play_number_guessing_game(max_guess_limit, target_between)
    total_win += win
    total_lose += lose
    game_play += play
    
    # New feature to add 
    # tracking the fewest number of attempts it took to win
    if win == 1:
        if best_score == []:
            best_score.append(attempt)
        
        else:
            for i in best_score:
                if i > attempt:
                    best_score = [attempt]

    # Replay input validation
    while True:

        replay = input(f"Do you want to play again? y/n: ").strip().lower()

        if replay == "y" or replay == "n":
            break
        else:
            print(f"\n❌ Invalid input! Please enter 'y' for yes and 'n' for no.\n")

    
    if replay == "n":
        print(f"\n🥳 Game End!\n")
        if len(best_score) > 0:
            print(f"🎉 New Record {best_score[0]}")
        else:
            print(f"No wins yet")
        print(f"▶️  You played {game_play} round.")
        print(f"🏆 Won {total_win} & 😔 Lost {total_lose}.\n")
        break
        
    else:
        continue


#next feature Dynamic Difficulty
#Tier" Strategy or the really cool "Math" Strategy! that use search engine 
