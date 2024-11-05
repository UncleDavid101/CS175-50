def get_grade():
    grade = float(input("Enter the grade: "))
    print(f"Grade entered: {grade}")
    return grade

def letter_grade(percentage_grade):
    if percentage_grade >= 90:
        print("A")
    elif percentage_grade >= 80:
        print("B")
    elif percentage_grade >= 70:
        print("C")
    elif percentage_grade >= 60:
        print("D")
    else:
        print("F")

def main():
    grade1 = get_grade()
    grade2 = get_grade()
    grade3 = get_grade()
    
    total = grade1 + grade2 + grade3
    percentage = total / 3
    print(f"Your final grade percentage is: {percentage}")
    
    print(f'You passed with a Grade {letter_grade(percentage)}')

if __name__ == "__main__":
    main()
