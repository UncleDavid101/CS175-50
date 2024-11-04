x = input('This is a vowel counter program. Please enter a string: ')
vowels = 'aeiou'
count = 0
for i in x:
    if i in vowels:
        count += 1
print('The number of vowels in the string is: ', count)