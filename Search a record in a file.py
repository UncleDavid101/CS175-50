def search_employee():
    search_value = input("Enter the name to search: ")

    try:
        with open('employee.txt', 'r') as file:
            found = False
            for line in file:
                name, *other_fields = line.strip().split(',')
                if name == search_value:
                    print(f"Record found: {line.strip()}")
                    found = True
                    break
            if not found:
                print("Error: Record not found.")
    except FileNotFoundError:
        print("Error: The file 'employee.txt' does not exist.")

if __name__ == "__main__":
    search_employee()
