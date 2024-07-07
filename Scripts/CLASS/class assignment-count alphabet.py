#Input some text from the user and count the number of vowels in the text
#also, capitalize all the vowels

text = input("Enter text: ")
vowel_count = 0

capital_text = " "

for char in text:
    if (char.lower() in 'aeiou'):
        vowel_count +=1
        capital_text += char.upper()
    else:
        capital_text += char

print("Number if vowels : ", vowel_count)
print("Text with vowels in capital :", capital_text)