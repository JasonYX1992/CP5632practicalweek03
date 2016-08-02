def is_valid_format():

    name = input("Please enter your name:")

    name = name.strip()

    if not name:
        print("The name is empty!")

    while not name:
        name = input("Please enter your name:")
        name = name.strip()

    for char in range(1, len(name), 3):
        print(name[char])

is_valid_format()