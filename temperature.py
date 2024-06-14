
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to handle temperature conversion based on user R
def temperature_converter():
    
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (Celsius, Fahrenheit, or Kelvin): ").lower()

    # Based on the user input, perform the appropriate conversion and display the results
    if unit == 'celsius':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif unit == 'fahrenheit':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif unit == 'kelvin':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid unit entered. Please enter Celsius, Fahrenheit, or Kelvin.")

# Call the function to start the temperature conversion process
temperature_converter()
