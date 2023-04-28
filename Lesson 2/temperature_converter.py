temperature_in_calcium = int(input('Please, enter temperature in t°C: '))
temperature_in_fahrenheit = (temperature_in_calcium * 9 / 5) + 32
temperature_in_kelvin = temperature_in_calcium + 273.16
print(f'Temperature in Fahrenheit: {temperature_in_fahrenheit} °F' + '\n' +
      f'Temperature in Kelvin: {temperature_in_kelvin} K')
