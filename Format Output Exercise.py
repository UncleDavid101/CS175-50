num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

sumproduct = "Sum"
differnceproduct = "Difference"
productproduct = "Product"
divisionproduct = "Integer division"
averageproduct = "Average"
remainderproduct = "Remainder"
powerproduct = "Exponet"

sum = num1 + num2
differnce = num1 - num2
product = num1 * num2
division = num1 / num2
average = (num1 + num2) / 2
remainder = num1 % num2
power = num1 ** num2



print()
print(f'{sumproduct:<25}', f'{sum:>20}')
print(f'{differnceproduct:<25}', f'{differnce:>20}')
print(f'{productproduct:<25}', f'{product:>20}')
print(f'{divisionproduct:<25}', f'{division:>20}')
print(f'{averageproduct:<25}', f'{average:>20}')
print(f'{remainderproduct:<25}', f'{remainder:>20}')
print(f'{powerproduct:<25}', f'{power:>20}')






'''
print("The sum of the two number is ", num1 + num2)
print("The difference of the two numbers is ", num1 - num2)
print("The prduct of the two numbers is ", num1 * num2)
print("The division of the two number is ", num1 / num2)
print("The average of the two numbers is", (num1 + num2) / 2)
print("The remainder of the two numbers is", num1 % num2)
print("The power of the two numbers is", num1 ** num2)
'''