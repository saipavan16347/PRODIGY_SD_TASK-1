def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
  """Converts Celsius to Kelvin."""
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
  """Converts Fahrenheit to Kelvin."""
  return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
  """Converts Kelvin to Celsius."""
  return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
  """Converts Kelvin to Fahrenheit."""
  return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
  """Prompts the user for input and performs temperature conversion."""

  try:
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit (Celsius, Fahrenheit, or Kelvin): ").lower()

    if unit == "celsius":
      fahrenheit = celsius_to_fahrenheit(temperature)
      kelvin = celsius_to_kelvin(temperature)
      print(f"{temperature} degrees Celsius is equal to:")
      print(f"{fahrenheit:.2f} degrees Fahrenheit")
      print(f"{kelvin:.2f} Kelvin")

    elif unit == "fahrenheit":
      celsius = fahrenheit_to_celsius(temperature)
      kelvin = fahrenheit_to_kelvin(temperature)
      print(f"{temperature} degrees Fahrenheit is equal to:")
      print(f"{celsius:.2f} degrees Celsius")
      print(f"{kelvin:.2f} Kelvin")

    elif unit == "kelvin":
      celsius = kelvin_to_celsius(temperature)
      fahrenheit = kelvin_to_fahrenheit(temperature)
      print(f"{temperature} Kelvin is equal to:")
      print(f"{celsius:.2f} degrees Celsius")
      print(f"{fahrenheit:.2f} degrees Fahrenheit")

    else:
      print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

  except ValueError:
    print("Invalid input. Please enter a valid number for the temperature.")

if __name__ == "__main__":
  temperature_converter()