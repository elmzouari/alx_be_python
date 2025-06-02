# Temperature Conversion Tool

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    celsius = (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FREEZING_POINT_OFFSET
    return fahrenheit

def get_temperature_input():
    """Get temperature input from user."""
    while True:
        try:
            temp_str = input("Enter the temperature to convert: ")
            temperature = float(temp_str)
            return temperature
        except ValueError:
            print("Please enter a valid numeric temperature.")

def get_unit_input():
    """Get unit input from user."""
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            return unit
        else:
            print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    """Main function to run the temperature conversion tool."""
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    try:
        # Get inputs
        temperature = get_temperature_input()
        unit = get_unit_input()
        
        # Perform conversion
        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:  # unit == 'F'
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
