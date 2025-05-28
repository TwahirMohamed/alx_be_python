# A Python script that will prompt the user to enter two numbers and select an operation(addition, subtraction, multiplication or division). The script will then perform the selected operation using match case statement and display the result.
# prompt the user for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask for type of operation they would like to perform
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+" :
        result = num1 + num2
        print(f"The result is {result}.")
    case "-" :
        result = num1 - num2
        print(f"The result is {result}.")
    case "*" :
        result = num1 * num2
        print(f"The result is {result}.")
    case "/" if num2 != 0 :
        result = num1 / num2
        print(f"The result is {result}.")
    case "/" if num2 == 0:
        print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")