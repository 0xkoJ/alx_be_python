FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit -32)* FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * convert_to_fahrenheit) + 32
def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert:"))
            unit = input("Enter unit (C/F): ").upper()
            if unit == "C":
                fahrenheit = convert_to_fahrenheit(temperature)
                print(f"{temperature} °C is equal to {fahrenheit:.2f}°F") 
            elif unit == "F":
                celsius = convert_to_celsius(temperature)
                print(f"{temperature}°F is equal to {celsius:.2f}°C")
            else:
                print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
