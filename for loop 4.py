
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_count = 0
odd_count = 0

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_count += 1
        even_numbers.append(number)
    else:
        odd_count += 1
        odd_numbers.append(number)

print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")