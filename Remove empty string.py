def remove_empty_strings(input_list):
    non_empty_strings = []
    for string in input_list:
        if string.strip():
            non_empty_strings.append(string)
    return non_empty_strings

# Sample lists of strings
list1 = ['', '  a  ', 'b', ' ', 'c  ']
list2 = ['d', '    ', ' efg', 'h i']
list3 = ['j k', 'lm', '        ', 'n o', '']

# Testing the function
print(remove_empty_strings(list1))  # Output: ['  a  ', 'b', 'c  ']
print(remove_empty_strings(list2))  # Output: ['d', ' efg', 'h i']
print(remove_empty_strings(list3))  # Output: ['j k', 'lm', 'n o']

list4 = []
