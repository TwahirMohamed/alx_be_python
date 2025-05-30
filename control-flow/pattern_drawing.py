# A python script which will prompt the user to enter a positive integer then use nested loops to print a square pattern of that size made of asterisks(*)
length = int(input("Enter the size of the pattern: "))

# checking if not zero
if length <= 0:
    print("Number must be positive")
else:
    row = 0
    while row < length:
        for col in range(length) :
            print("*", end="")
        print()
        row += 1
