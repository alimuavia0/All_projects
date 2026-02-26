import os
import re

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data.txt")

with open(file_path, "r") as file:
    content = file.read().lower()

# Extract words
words = re.findall(r"[A-Za-z]\w*(?:\-[A-Za-z]\w*)?", content)

total_vowels = 0
total_cons = 0
total_letters = 0
total_words = 0
word_freq = {}
largest_word = ""

vowels = "aeiou"

for word in words:
    
    total_words += 1
    
    # Largest word
    if len(word) > len(largest_word):
        largest_word = word
    
    # Word frequency
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
    
    # Letters count
    for char in word:
        total_letters += 1
        
        if char in vowels:
            total_vowels += 1
        elif char.isalpha():
            total_cons += 1

print("Total letters:", total_letters)
print("Total words:", total_words)
print("Largest word:", largest_word)
print("Total Consonants:", total_cons)
print("Total Vowels:", total_vowels)
# print("Word frequency:", word_freq)

