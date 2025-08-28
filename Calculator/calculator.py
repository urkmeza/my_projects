from functions import *

while True:

    print("What do you want to do?")
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press Q to Exit")

    choice = input("Enter your choice: ")
    if choice == "q" or choice == "Q":
        break

    num1 = float(input ("Enter number 1:"))
    num2 = float(input ("Enter number 2:"))

    if choice == "1":
        addition(num1, num2)
    elif choice == "2":
        subtraction(num1, num2)
    elif choice == "3":
        multiplication (num1, num2)
    elif choice == "4":
        division (num1, num2)
    else:
        print("Invalid Choice!")
    
    
    print("\n")