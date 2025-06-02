# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FREEZING_POINT_OFFSET

def main():
    print("Temperature Conversion Tool")
    print("-" * 26)
    
    try:
        # Get temperature input
        temp_str = input("Enter the temperature to convert: ")
        temperature = float(temp_str)
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
        
        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("Error: Please enter a valid numeric value for temperature.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
