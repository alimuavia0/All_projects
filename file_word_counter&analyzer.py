
#data for read from file
file = open ('','r')

# data read line by line 
lines = readlines(file)

total_vowels = 0
total= 0
total_cons = 0
largest_word = 0
total_words = 0
word_freq = {}
#split data in line 
for line in lines :
    
    # remove white spaces
    line = lines.strip()
    
    # split lines in words & convert in lower case 
    words = line.split().lower()
    for lin in line :
        
        #find largest word
        if largest_word > Len(lin) :
          largest_word = lin
          
    # count total words 
    for word in words :
        total_words += word
        
        #count frequency of each word
        if word_freq in words :
            word_freq[word] += 1
        else :
           word_freq[word] = 1
          
   #filter data in vowels & consonants 
    vowels = 'aeiou'
    for I in words :
        if I in vowels :
           total_vowels += I
           
        else : 
           total_cons += I

file.close()

print("total letters:",total)
print("total wors:",total_words)
print("Largest wors:", largest_word)
print("total Consonants:",total_cons)
print("total Vowels:",total_vowels)
print("Words frequency:",word_freq)

