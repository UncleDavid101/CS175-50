def sum_numbers_in_file(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    
    
    
    total = sum(numbers)
    print(f"Numbers: {numbers[0]}, {numbers[1]}, {numbers[2]}")
    print(f"Total: {total}")

sum_numbers_in_file('numbers.txt')
