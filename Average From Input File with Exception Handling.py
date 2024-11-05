def read_values_from_file(filename):
    values = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    values.append(float(line.strip()))
                except ValueError:
                    print(f"Warning: Could not convert line to float: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return values

def calculate_average(values):
    if not values:
        return None
    return sum(values) / len(values)

def print_average(average):
    if average is None:
        print("No valid data to calculate an average.")
    else:
        print(f"The average is: {average}")

def main():
    filename = 'data.txt' 
    values = read_values_from_file(filename)
    average = calculate_average(values)
    print_average(average)

if __name__ == "__main__":
    main()
