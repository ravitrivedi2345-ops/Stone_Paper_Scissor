import game_logic

def show_menu():
    print("\n--- STONE PAPER SCISSOR ---")
    print("1. Play Game")
    print("2. Exit")
    print("---------------------------")

def play_round():
    print("\nChoose an option:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissor")
    
    choices_map = {'1': 'stone', '2': 'paper', '3': 'scissor'}
    
    user_input = input("Enter your choice (1-3): ").strip()
    
    if user_input not in choices_map:
        print("Invalid choice! Please select 1, 2, or 3.")
        return
        
    user_choice = choices_map[user_input]
    computer_choice = game_logic.get_computer_choice()
    
    print(f"\nYou chose     : {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    result = game_logic.determine_winner(user_choice, computer_choice)
    
    print("-" * 25)
    if result == 'tie':
        print("Result: It's a Tie!")
    elif result == 'user':
        print("Result: You Win! 🎉")
    else:
        print("Result: Computer Wins! 💻")
    print("-" * 25)

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-2): ").strip()
        
        if choice == '1':
            play_round()
        elif choice == '2':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
