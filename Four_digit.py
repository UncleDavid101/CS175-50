x = int(input("Enter a four-digit number: "))
while x < 1000 or x > 9999:
    print("Your input was four digits.")


last_digit = x % 10
remaining = x // 10
second_last_digit = remaining % 10
remaining = remaining // 10
third_last_digit = remaining % 10
remaining = remaining // 10
first_digit = remaining % 10
sum = first_digit + second_last_digit + third_last_digit + last_digit


print(f"The sum of the digits is {sum}.")
print(f'The digits are {first_digit}, {second_last_digit}, {third_last_digit}, {last_digit}.')