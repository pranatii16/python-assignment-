from collections import Counter
import re

def count_word_frequency(paragraph):
    # Convert to lowercase to make counting case-insensitive
    paragraph = paragraph.lower()
    
    # Use regex to extract words (ignoring punctuation)
    words = re.findall(r'\b\w+\b', paragraph)
    
    # Count word frequencies
    word_freq = Counter(words)
    
    return word_freq

# Get paragraph input from the user
paragraph = input("Enter a paragraph: ")

# Get word frequencies
frequencies = count_word_frequency(paragraph)

# Display the word frequencies
print("\nWord Frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")
