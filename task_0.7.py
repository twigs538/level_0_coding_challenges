def celcius_to_fahrenheit(temperature):
    fahrenheit = (temperature * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celcius(temperature):
    celcius = (temperature - 32) * 5 / 9
    return celcius

print(celcius_to_fahrenheit(0))
print(fahrenheit_to_celcius(32))