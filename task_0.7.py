def celsius_degrees_to_fahrenheit_degrees(temperature):
    fahrenheit = (temperature * 9 / 5) + 32
    return fahrenheit

def fahrenheit_degrees_to_celsius_degrees(temperature):
    celsius = (temperature - 32) * 5 / 9
    return celsius

if __name__ == '__main__':
    print(celsius_degrees_to_fahrenheit_degrees(0))
    print(fahrenheit_degrees_to_celsius_degrees(32))