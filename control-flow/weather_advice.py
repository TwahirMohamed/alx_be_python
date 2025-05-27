# A python script that asks the user about current weather conditions and provide clothing recommendations based on the input.
# The task aims to demonstrate the use of if,elif and else statements to make decision in a program.

# prompt user for weather input
condition = input("What's the weather like today? (sunny/rainy/cold):")

# provide clothing recommendations
if condition == "sunny":
    message = "Wear a t-shirt and sunglasses."
elif condition == "rainy":
    message = "Don't forget your umbrella and a raincoat."
elif condition == "cold":
    message = "Make sure to wear a warm coat and a scarf."
else:
    message = "Sorry, I don't have recommendations for this weather."

print(message)
