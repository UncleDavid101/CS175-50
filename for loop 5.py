numbers = [3, 5, 7, 2, 8, -1, 4]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")