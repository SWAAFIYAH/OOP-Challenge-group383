import time
from pet import Pet, clear_screen

def main():
    # Creating a pet
    clear_screen()
    print("Creating your pet", end="")
    
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
        
    print("\n")

	#  Naming the pet
    pet = Pet("Cuty")
    
    while True:
        clear_screen()
        
        pet.animate_pet()
        
		# Diplaying pet's status and user options
        print(pet.get_status())
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Train")
        print("5. Show tricks")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

		# If...else statement for user input
        if choice == "1":
            print(pet.eat())
        elif choice == "2":
            print(pet.sleep())
        elif choice == "3":
            print(pet.play())
        elif choice == "4":
            print("\nAvailable tricks to learn:")
            
            for i, trick in enumerate(pet.available_tricks, 1):
                print(f"{i}. {trick}")
                
            trick_choice = input("\nChoose a trick number to learn: ")
            
            try:
                trick_index = int(trick_choice)
                
                if 1 <= trick_index <= len(pet.available_tricks):
                    print(pet.train(trick_index))
                else:
                    print("Invalid trick number!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "5":
            print(pet.show_tricks())
        elif choice == "6":
            print(f"\nGoodbye! Take care of {pet.name}!")
            break
        else:
            print("Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()