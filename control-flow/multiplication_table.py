# A python script that uses for loop to print the multiplication table for that number from 1 to 10
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 10):
    print(f"{number} * {i} = {number * i}")