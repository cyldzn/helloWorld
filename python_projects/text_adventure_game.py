"""A very simple text-based adventure game."""

def intro():
    print("You wake up in a dark room with two doors.")
    print("1. Open the left door")
    print("2. Open the right door")
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        left_room()
    elif choice == '2':
        right_room()
    else:
        print("Invalid choice")


def left_room():
    print("The room is empty. You return and choose again.")
    intro()


def right_room():
    print("You find a treasure chest! Congratulations, you win!")


def main():
    intro()


if __name__ == "__main__":
    main()
