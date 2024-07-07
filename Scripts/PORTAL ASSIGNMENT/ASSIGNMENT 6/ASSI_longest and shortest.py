'''
Input a sequence of words from the user, and output the shortest and longest word in the sequence
Example: Input: apple ball cat
 Output:
Shortest: cat
Longest: apple

'''
text = input("Enter some text: ")
string = text 
word = "";  
words = [];   
string = string + " ";  
   
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        word = word + string[i];  
    else:  
        words.append(word);  
        word = "";  
small = large = words[0];  
for k in range(0, len(words)):  
    if(len(small) > len(words[k])):  
        small = words[k];  
    if(len(large) < len(words[k])):  
        large = words[k];    
print("Smallest word: " + small);  
print("Largest word: " + large);  