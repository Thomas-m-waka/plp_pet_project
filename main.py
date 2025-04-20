from pet import Pet

print("🐶 Welcome to the Virtual Pet Game!")
pet_name = input("What would you like to name your pet? ")
pet = Pet(pet_name)

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Feed your pet 🍗")
    print("2. Let your pet sleep 🛌")
    print("3. Play with your pet 🐾")
    print("4. Check status 📊")
    print("5. Teach a trick 🎓")
    print("6. Show learned tricks 🎪")
    print("7. Exit ❌")

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        pet.eat()
    elif choice == "2":
        pet.sleep()
    elif choice == "3":
        pet.play()
    elif choice == "4":
        pet.get_status()
    elif choice == "5":
        trick = input("What trick do you want to teach? ")
        pet.train(trick)
    elif choice == "6":
        pet.show_tricks()
    elif choice == "7":
        print(f"Goodbye! {pet.name} will miss you! 🐾")
        break
    else:
        print("Invalid choice. Try again!")

