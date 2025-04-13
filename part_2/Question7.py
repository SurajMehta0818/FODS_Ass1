def count_letters_digits(input_string):
    letters = 0
    digits = 0
    
    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    
    return letters, digits

# Get input from user
user_input = input("Enter a string: ")

# Calculate counts
letter_count, digit_count = count_letters_digits(user_input)

# Display results
print(f"\nAnalysis of the string:")
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Other characters: {len(user_input) - (letter_count + digit_count)}")