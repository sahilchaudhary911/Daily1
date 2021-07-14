# Modify the previous program such that only the users Alice and Bob are greeted with their names.


def greeting_alice_and_bob():
    user = input("Enter your name: ")
    name = ["Alice", "Bob"]
    if user == name[0] or name == name[1]:
        print(f"Hello {user}!")


greeting_alice_and_bob()