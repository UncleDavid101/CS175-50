def createRecords():
    num_records = int(input("Enter the number of employee records to create: "))
    
    with open("employee.txt", "w") as file:
        for _ in range(num_records):
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            position = input("Enter employee position: ")
            
            file.write(f"{name},{age},{position}\n")

createRecords()
