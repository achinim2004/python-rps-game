import random

def play_game():
   
    

    choices = ["Rock", "Paper", "Scissors"]
    
   
    rules = {
        "Rock": "Scissors",    
        "Paper": "Rock",       
        "Scissors": "Paper"    
    }
    

    while True:
        print("\n--- New Round ---")
        
        # Computer's choice (using random.choice())
        computer_choice = random.choice(choices)
        
   
        print("What is your choice?")
        print("1: Rock")
        print("2: Paper")
        print("3: Scissors")
        print("4: Quit")
        
        user_input = input("Enter a number (1/2/3/4): ")
        
        if user_input == '4':
            print("Game over. Goodbye!")
            break  
            
        if user_input not in ['1', '2', '3']:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            continue 
            
        # Convert user input number to the choice string
        user_choice = choices[int(user_input) - 1]
        
     
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
      
        if user_choice == computer_choice:
            print("It's a tie!")
            
        elif rules[user_choice] == computer_choice:
            print("🥳 You win!")
            
        else:
            print("😥 The computer wins.")

if __name__ == "__main__":
    play_game()