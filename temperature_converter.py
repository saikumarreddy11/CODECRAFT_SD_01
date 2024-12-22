def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return ((f - 32) * 5/9) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return ((k - 273.15) * 9/5) + 32

def temperature_conversion():
    print("Temperature Conversion Program")
    print("Choose the input unit:")
    print("1. Celsius\n2. Fahrenheit\n3. Kelvin")
    
    choice = int(input("Enter your choice (1/2/3): "))
    temp = float(input("Enter the temperature value: "))
    
    if choice == 1:
        print(f"{temp}°C is equivalent to:")
        print(f"{celsius_to_fahrenheit(temp):.2f}°F")
        print(f"{celsius_to_kelvin(temp):.2f}K")
    elif choice == 2:
        print(f"{temp}°F is equivalent to:")
        print(f"{fahrenheit_to_celsius(temp):.2f}°C")
        print(f"{fahrenheit_to_kelvin(temp):.2f}K")
    elif choice == 3:
        print(f"{temp}K is equivalent to:")
        print(f"{kelvin_to_celsius(temp):.2f}°C")
        print(f"{kelvin_to_fahrenheit(temp):.2f}°F")
    else:
        print("Invalid choice! Please run the program again.")

if __name__ == "__main__":
    temperature_conversion()
