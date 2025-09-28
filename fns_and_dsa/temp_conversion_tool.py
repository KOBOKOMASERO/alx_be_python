# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius using the global factor.
    Formula: (F - 32) * 5/9
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit using the global factor.
    Formula: (C * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt the user for temperature
        temperature = input("Enter the temperature to convert: ").strip()

        # Validate that the temperature is numeric
        if not temperature.replace('.', '', 1).isdigit() and not (
            temperature.startswith('-') and temperature[1:].replace('.', '', 1).isdigit()
        ):
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temperature)

        # Ask for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            # Fahrenheit to Celsius conversion
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == 'C':
            # Celsius to Fahrenheit conversion
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Display error message for invalid temperature input
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
