# A python script that asks the user about current weather conditions and provide clothing recommendations based on the input.
# The task aims to demonstrate the use of if,elif and else statements to make decision in a program.

# prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

# provide clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif  weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

