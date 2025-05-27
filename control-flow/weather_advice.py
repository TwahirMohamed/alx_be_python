# A python script that asks the user about current weather conditions and provide clothing recommendations based on the input.
# The task aims to demonstrate the use of if,elif and else statements to make decision in a program.

# prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

# provide clothing recommendations
if weather == "sunny":
    message = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    message = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    message = "Make sure to wear a warm coat and a scarf."
else:
    message = "Sorry, I don't have recommendations for this weather."

print(message)
