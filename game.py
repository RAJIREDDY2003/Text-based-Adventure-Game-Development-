import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to reach the magical portal at the end of the forest.")
    time.sleep(1)

def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest_path():
    print("\nYou start walking through the forest.")
    time.sleep(1)
    print("You come across a fork in the path.")
    time.sleep(1)

    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou follow the left path.")
        time.sleep(1)
        return "left_path"
    else:
        print("\nYou follow the right path.")
        time.sleep(1)
        return "right_path"

def left_path():
    print("\nYou encounter a friendly wizard who offers you a magical map.")
    time.sleep(1)

    choices = ["Accept the map", "Decline the map"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nThe wizard gives you the map. It reveals a shortcut.")
        time.sleep(1)
        return "shortcut"
    else:
        print("\nYou politely decline and continue on the path.")
        time.sleep(1)
        return "continue"

def right_path():
    print("\nYou stumble upon a pack of wolves blocking the path.")
    time.sleep(1)

    choices = ["Attempt to sneak past", "Confront the wolves"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou successfully sneak past the wolves.")
        time.sleep(1)
        return "continue"
    else:
        print("\nThe wolves attack! You defend yourself and continue.")
        time.sleep(1)
        return "continue"

def shortcut():
    print("\nThe map leads you to a magical shortcut.")
    time.sleep(1)
    print("You reach the magical portal and win the game!")

def continue_path():
    print("\nYou continue on the path.")
    time.sleep(1)
    print("You encounter a mystical creature guarding the portal.")
    time.sleep(1)

    choices = ["Befriend the creature", "Fight the creature"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou befriend the creature, and it allows you to pass.")
        time.sleep(1)
        print("You reach the magical portal and win the game!")
    else:
        print("\nYou engage in a fierce battle with the creature.")
        time.sleep(1)
        print("Unfortunately, you are defeated. Game over.")

def main():
    introduction()
    current_location = forest_path()

    if current_location == "left_path":
        current_location = left_path()
    elif current_location == "right_path":
        current_location = right_path()

    if current_location == "shortcut":
        shortcut()
    elif current_location == "continue":
        continue_path()

if __name__ == "__main__":
    main()
