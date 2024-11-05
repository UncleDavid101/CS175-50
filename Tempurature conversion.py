def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fareinheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    cf = float(input('1 to convert celsius to fahrenheit, 2 to convert fahrenheit to celsius: '))
    if cf == 1:
        celsius = float(input('Enter a temperature in Celsius: '))
        print(f'The temperature in Fahrenheit is {celsius_to_fahrenheit(celsius):.2f}')
    elif cf == 2:
        fareinheit = float(input('Enter a temperature in Fahrenheit: '))
        print(f'The temperature in Celsius is {fareinheit_to_celsius(fareinheit):.2f}')

if __name__ == '__main__':
    main()