def convert_temp(temp:float, Fahrenheit = False):
  if Fahrenheit == False:
    if temp<-273.15:
      raise ValueError("Temperature below absolute zero is invalid for Celsius.")
    elif temp == -273.15:
      return None
    else:
      farenheit = (9/5)*temp+32
      return round(farenheit,2)

  else:
    if temp<-459.67:
      raise ValueError("Temperature below absolute zero is invalid for Fahrenheit.")
    elif temp == -459.67:
       return None
    else:
      celcius = (5/9)*(temp-32)
      return round(celcius,2)


if __name__ == "__main__":
    # I would comment some of these out as you build up parts of convert_temp
    # e.g. just start by getting convert_temp(20) to work
    print(convert_temp(20)) # Prints 68.0
    print(convert_temp(-10)) # Prints 14.0
    print(convert_temp(68, Fahrenheit=True)) # Prints 20.0
    print(convert_temp(-100, Fahrenheit=True)) # Prints -73.33
    print(convert_temp(-300)) # ValueError("Temperature below absolute zero is invalid for Celsius.")
    print(convert_temp(-500, Fahrenheit=True)) # ValueError("Temperature below absolute zero is invalid for Fahrenheit.")