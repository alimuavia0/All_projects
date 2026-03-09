import os
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

text = input("Enter data: ")

content = text.lower()

# Extract words
words = re.findall(r"[A-Za-z]\w*(?:\-[A-Za-z]\w*)?", content)
numbers = re.findall(r"[0-9]\d*(?:\-[0-9]\d*)?", content)

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

# print("Total letters:", total_letters)
# print("Total words:", total_words)
# print("Largest word:", largest_word)
# print("Total Consonants:", total_cons)
# print("Total Vowels:", total_vowels)
# # print("Word frequency:", word_freq)



#data convert into row data
datas = [{
    'Total_letters':total_letters,
        'Total_Consonants':total_cons,
        'Total_Vowels':total_vowels,
        'Total_Words':total_words,
        'Total_Digits':len(numbers),
        # 'Largest_Word':largest_word,
        }]
#data into DataFrame
data = pd.DataFrame(datas)
print("1) Normally\n 2) In plots\n 3) Exit")

q = input("Enter which you want data: ")
atempts = 0
if q == "1" :
    print(data)
elif q == "2" :
    print("1) barplot\n 2)Pieplot\n 3) Exit")
    atempts = 1
elif q in ("3","exit"):
    print("Thanks for coming")
else :
    print("Invalid option")
while atempts :
    user = input("Enter which you want!: ").lower()
    print("Thanks for coming")
    if user in ("3","exit") :
        break
    atempts += 1
    if user == "1" :
        plt.figure(figsize=(8,5))
        sns.barplot(data=data)
        plt.title("The Data in Barplot")
        plt.ylabel("Counts")
        plt.xlabel("Largest_Word:" + largest_word)
        plt.show()
    elif user == "2" :
        data.drop(columns=["Largest_Word"], errors="ignore")
        values = data.iloc[0]     # first row values
        labels = data.columns     # column names
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.title("Data Analysis")
        plt.show()
    else : 
        print("Invalid option")
