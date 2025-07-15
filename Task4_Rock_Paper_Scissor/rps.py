import random

def main():
    try:
        options = ["rock", "paper", "scissors"]
        computer_score, user_score = 0,0

        while True:
            computer = random.choice(options).strip().lower()
            print(f"Your Score : {user_score} | Computer Score : {computer_score}")
            choice = input("\nPlay Rock-Paper-Scissors? (Yes/No) : ").strip().lower()
            if choice == "yes":
                user = input("Enter Your choice (Rock/Paper/Scissors) : ").strip().lower()
                if user not in options:
                    print("Invalid Option!, Try Again")
                    continue
                print(f"\nComputer chose: {computer.capitalize()}")
                print(f"You chose: {user.capitalize()}")
                if computer==user:
                    print("It's Tie!")
                elif (
                        (computer=="rock" and user=="scissors") or 
                        (computer=="paper" and user=="rock") or
                        (computer=="scissors" and user=="paper")
                    ):
                    print("Computer Wins!")
                    computer_score += 1
                else:
                    print("You Win!")
                    user_score += 1

            elif choice == "no":
                print("Thank You, Bye!")
                break
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
