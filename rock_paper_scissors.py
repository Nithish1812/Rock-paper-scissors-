import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        choice = input("Enter Rock, Paper, or Scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid input. Try again.")

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or          (user == "scissors" and computer == "paper") or          (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"You chose {user}, Computer chose {computer}")

        result = determine_winner(user, computer)

        if result == "draw":
            print("It's a draw!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()