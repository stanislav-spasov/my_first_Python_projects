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

# Apply the selected transformation
if choice == 1:
    transforming_text = text[::-1]
    print(transforming_text)
