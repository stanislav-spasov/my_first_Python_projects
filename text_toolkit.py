# Display a menu to the user
print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

# Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Get the input string
text = input("Enter the text: ")

# Supported variables
message = ""
transforming_text = ""
counter_vowels = 0
vowels = "aeiouAEIOU"

# Apply the selected transformation
if choice == 1:
    # Reverse text
    transforming_text = text[::-1]
    message = "Your text reverse: "
elif choice == 2:
    # Uppercase convert
    transforming_text = text.upper()
    message = "Your UPPERCASE text: "
elif choice == 3:
    # Lowercase convert
    transforming_text = text.lower()
    message = "Your lowercase text: "
elif choice == 4:
    # Title case
    transforming_text = text.title()
    message = "Your Title Text: "
elif choice == 5:
    # Count vowels
    for letter in text:
        if letter in vowels:
            counter_vowels += 1
    transforming_text = str(counter_vowels)
    message = "The count of vowels in your text is: "
elif choice == 6:
    # Remove spaces
    transforming_text = "".join(letter for letter in text if not letter.isspace())
    message = "You text without spaces: "
elif choice == 7:
    # Replace vowels with "*"
    for letter in text:
        if letter in vowels:
            letter = letter.replace(letter,'*')
        transforming_text += letter
    message = "Your text with vowels replaced with '*': "
elif choice == 8:
    # Palindrome check
    transforming_text = "".join(letter for letter in text if not letter.isspace()).lower()
    if transforming_text == transforming_text[::-1]:
        transforming_text = f"-> {text} <-"
        message = "Your text is palindrome: "
    else:
        message = "Your text is not palindrome: "
elif choice == 9:
    # Word frequency
    words = text.split()
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
    transforming_text = frequency
    message = "Result from word frequency counter is: "
else:
    # Invalid choice
    print("❌ Invalid choice! Please restart the program.")

# Print result
print(f"{message}{transforming_text}")
