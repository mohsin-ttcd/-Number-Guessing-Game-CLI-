# number guessing game

#import random module
import random

target_number = random.randint(0,20)
max_guess_limit = 5

print(f"***** Game Start *****")
print(f"*** Max guess limit {max_guess_limit} ***")
print(f"Enter number between 0 - 20\n")

while max_guess_limit > 0:

    try:
        user_input = int(input("Guess The Number: "))
    
    except ValueError:
        print("Please enter a integer number between 0 - 20")
        continue

    if user_input == target_number:
        print(f"\n🥇 You won the game!")
        print(f"🎯 Target number was {target_number}")
        print(f"🎮 You enter {user_input}\n")
        break
    
    elif user_input > target_number:
        print(f"\n❌ Too high!")
        print("🔄️ Try again!\n")

    else:
        print("\n❌ Too low!")
        print("🔄️ Try again!\n")

    max_guess_limit = max_guess_limit - 1

if max_guess_limit == 0:
    print("\n❌ Game Over!")
    print("❌ You hit the max limit!\n")