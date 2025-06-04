# A python script with a function that perfoms basic arithmetic operations. The function will be imported and used in a separate main file.
def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0:
                return num1 / num2
            else:
                print("Division by zero is not possible:")
        case _:
            print("Unrecognized type of operation.")