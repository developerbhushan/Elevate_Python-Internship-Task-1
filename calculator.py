# calculator.py

def add(x, y):                # Addition Function Definition
    return x + y

def substract(x, y):          # Subsrction Function Definition
    return x - y

def multiplication(x, y):     # Multiplication Function Definition
    return x * y

def division(x, y):           # Division Function Definition
    if y == 0:
        print("Error.! Division by zero is not allowed..")

    return x / y

# Main Program

while True:
    print("\n---- Calculator Menu---------")
    print("1. Additon (+)")
    print("2. Substraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter Your Choise (1-5): ")

    if choice == '5':
        print(f"Thanks For Using Our Smart Calculator...Come Again!!!")
        break

    if choice in ['1','2','3','4','5']:
        try:
            num1 = float(input("Enter First Number: "))        # Taking Inputs form user
            num2 = float(input("Enter Second Number: "))
            
        except ValueError:
            print("Invalid Input! Please enter numeric..")
            continue

        if choice == '1':
            addition = add(num1,num2)
            print("*"*50)
            print(f"Addtion Of {num1} and {num2} is {addition}")
            print("*"*50)
        
        elif choice == '2':
            sub = substract(num1, num2)
            print("*"*50)
            print(f"Substraction Of {num1} and {num2} is {sub}")
            print("*"*50)

        elif choice == '3':
            mul = multiplication(num1, num2)
            print("*"*50)
            print(f"Multiplication Of {num1} and {num2} is {mul}")
            print("*"*50)

        elif choice == '4':
            div = division(num1, num2)
            print("*"*50)
            print(f"Division Of {num1} and {num2} is {div}")
            print("*"*50)

    else:
        print("Invalid Choice ! Please Select a valid option betwee (1-5)..")