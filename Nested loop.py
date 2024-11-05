Outer_loop = int(input("Enter range of outside loop: "))
inside = 4  # Fixed number of iterations for the inner loop
total = 0  # Initialize the total sum to zero

for i in range(Outer_loop):
    print("Outer loop iteration: ", i + 1)
    for j in range(inside):
        total += int(input('Enter a number: '))

cycles = Outer_loop * inside
print("Total number of cycles: ", cycles)
print("Total sum: ", total)