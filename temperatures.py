"""
Transfer celsius to fahrenheit or fahrenheit to celsius
"""


def temperatures():
    MENU = "C - celsius to fahrenheit\nF - fahrenheit to celsius\nQ-Quit"
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius:"))
            transfer_to_celsius(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:"))
            transfer_to_fahrenheit(fahrenheit)
        else:
            print("Invalid value")
        print(MENU)
        choice = input(">>>").upper()
    print("Thanks")


def transfer_to_celsius(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(fahrenheit)


def transfer_to_fahrenheit(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print(celsius)

temperatures()