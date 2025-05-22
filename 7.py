def find_longest_word(sentence):
    words = sentence.split() 
    longest_word = ""
    for word in words:
        
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


sentence = input("Enter a sentence: ")
longest = find_longest_word(sentence)
print("The longest word is:", longest)