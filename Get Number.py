def get_number(lower, upper):

  number = True

  while number:

     try:
         num = int(input("please enter a number:"))

     except ValueError:
         print("please enter a valid number")

     else:
         if num < lower or num > upper:
             print("please enter a valid number")

         else:
            number = False

  print("you enter is " + str(num))


get_number(10, 50)

