from create_strong_password import create_strong_password
from gen_random_password import gen_random_password


def menu():
    print("-- Password generator --")
    print("What do you want to do")
    print("1 - Generate a fully random password")
    print("2 - Create a strong password easy to remember")

    choice = input("Your choice: ")

    if choice == "1":
        gen_random_password()
    elif choice == "2":
        create_strong_password()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    menu()
