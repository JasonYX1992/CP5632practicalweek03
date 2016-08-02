def get_number(lower, upper):

  num = int(input("please enter a number:"))

  while num < lower or num > upper:
      print("Please enter a valid number!")
      num = int(input("please enter a number:"))

  print("you enter is " + str(num))


get_number(10, 50)

