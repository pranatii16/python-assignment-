from collections import Counter

def count_character_frequency(text):
    # Remove spaces
    text = text.replace(" ", "")
    
    # Convert to lowercase (optional, for case-insensitive counting)
    text = text.lower()
    
    # Count character frequencies
    char_freq = Counter(text)
    
    return char_freq

# Get input from the user
text = input("Enter a string: ")

# Get character frequencies
frequencies = count_character_frequency(text)

# Display the character frequencies
print("\nCharacter Frequencies:")
for char, count in frequencies.items():
    print(f"{char}: {count}")
