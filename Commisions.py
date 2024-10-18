#CS175
#David Thomas II
x = True
while x == True:
    ss = float(input("Enter salesperson's sales: "))
    cr = float(input("Enter salesperson's commission rate: "))
    commision = (ss * cr) / 100
    print("Salesperson's commission: ", commision)
    x = input("Would you like to calculate another commission? (y/n): ")
    if x == 'y':
        x = True
    else:
        x = False
