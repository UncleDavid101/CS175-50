def get_input():
    wage = float(input("Enter your wage: "))
    hours = float(input("Enter the number of hours you worked: "))
    return wage, hours

def weekly_pay(wage, hours):
    if hours <= 40:
        return wage * hours
    else:
        return wage * 40 + (wage * 1.5 * (hours - 40))

wage, hours = get_input()
print('Weekly pay: ', weekly_pay(wage, hours))
