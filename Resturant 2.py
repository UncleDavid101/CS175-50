#CS175
#First name Last name
#restaurant
vegetarian = False
vegan = False
gluten_free = False
vegetarian = input("Is anyone in your party a vegetarian? ")
if vegetarian == "yes":
    vegetarian = True
else: vegetarian = False
vegan = input("Is anyone in your party a vegan? ")
if vegan == "yes":
    vegan = True
else: vegan = False
gluten_free = input("Is anyone in your party gluten-free? ")
if gluten_free == "yes":
    gluten_free = True
else: gluten_free = False
print(f'Here are your restaurant choices: ')
if not vegetarian and not vegan and not gluten_free:
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
    print("Corner Cafe")
elif not vegan and not gluten_free:
    print("Main Street Pizza Company")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
    print("Corner Cafe")
elif not vegetarian and not vegan:
    print("Main Street Pizza Company")
    print("The Chef's Kitchen")
    print("Corner Cafe")
elif not vegan:
    print("Main Street Pizza Company")
    print("The Chef's Kitchen")
    print("Corner Cafe")
elif not vegetarian and not gluten_free:
    print('Corner Cafe')
    print('The Chef\'s Kitchen')
elif not vegetarian:
    print('Corner Cafe')
    print('The Chef\'s Kitchen')
elif not gluten_free:
    print('Corner Cafe')
    print('The Chef\'s Kitchen')
else:
    print('Corner Cafe')
    print('The Chef\'s Kitchen')

    