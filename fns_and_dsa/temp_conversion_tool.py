# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if scale == "C":
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    elif scale == "F":
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
