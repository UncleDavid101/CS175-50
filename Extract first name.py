def extract_first_name(full_name):
    return full_name.split()[0]

def main():
    full_name = input("Enter your full name: ")
    first_name = extract_first_name(full_name)
    print("Your first name is", first_name)

if __name__ == '__main__':
    main()