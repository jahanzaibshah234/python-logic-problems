"""Problem: Count Vowels and Consonants
Task:
Ask the user to enter a word or sentence.
Count the number of vowels and consonants.
Print both counts."""

# Pseudocode
# Get input from user
# Create a vowels varaible
# Initialize vowel counter
# Initialize consonant counter
# Lower input string for case sensitive
# For-loop to check vowel and consonants in input string

# Ask for user input
s = input("Enter a word: ")

# Create a vowels variable
vowels = "aeiou"

# Initialize vowel counter
vowel_count = 0

# Initialize consonant counter
consonant_count = 0

# Lower input string for case sensitive
input_string = s.lower()

# For loop to count vowels and consonants
for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowel Count:", vowel_count)
print("Consonant Count: ", consonant_count)

