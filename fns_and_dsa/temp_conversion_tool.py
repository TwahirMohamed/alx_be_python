# A python script to illustrate the concept of variable scope though a temperature conversion tool betweem celsius and farenheit using global variables to store conversion factors.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
def main():
    temperature = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if choice.lower() == 'c':
        convert_to_fahrenheit(temperature)
    elif choice.lower() == 'f':
        convert_to_celsius(temperature)
    else:
        print("Unknown operatiom.")

if __name__ == "__main__":
    main()