def name_in_box():
    name = input("Enter your name: ")
    print("+" + "-" * (len(name) + 2) + "+")
    print("| " + name + " |")
    print("+" + "-" * (len(name) + 2) + "+")    

name_in_box()
