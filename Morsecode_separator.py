#morse-code-and-word-separator
#Turning normal words to morse code




#List made for a new sentence and the adjusted sentence with spaces. And the INDEX variable is set to 0
new_sentence = []
adjust_sentence = []
convert_sentence = []
INDEX = 0
Indicator_2 = 1
space_2 = 1


#All the characters are put in the characters list. And with corresponding index, all of the morse code is set in the morse code list.
characters = [' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


morse_code = [' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']




#input for sentence that will be converted to morse code
sentence = input('Enter a sentence: ')


word = ' '.join(sentence)


# A first letter index variable is made so that there is no space at the start of the output sentence (before the first letter).
first_letter = word[0]
first_letter_index = sentence.index(first_letter)




# 2 main for loops are made to loop through each letter in the input sentence and each letter in the uppercase list.
# Then there is an if and elif statement to properly place the differnet spaces in the final sentence.
#I used 2 indicators to add a space directly after the first word and anywhere else needed in the output sentnece.
for i in range(len(sentence)):
  adjust_sentence.append(sentence[i])
  for w in range(len(uppercase)):
    Indicator = 1
    if uppercase[w] == sentence[i] and Indicator_2 == 0:
      space_3 = i + space_2 
      if i != first_letter_index:
        adjust_sentence.insert(space_3, ' ')
        space_2 += 1
        
    elif uppercase[w] == sentence[i] and Indicator == 1:
      Indicator = i
      if i != first_letter_index:
        adjust_sentence.insert(Indicator, ' ')
        Indicator_2 = 0
        Capital_letter = adjust_sentence[0]


final_sentence = ''.join(adjust_sentence)
words = final_sentence.lower()




# A for loop to set the first letter in the sentence to capital.
for i in range(len(adjust_sentence)):
  convert_sentence.append(words[i])
convert_sentence[0] = Capital_letter




# A for loop is set to look for any I standing on it's own so that it can be capitalized.
for i in range(len(adjust_sentence)):
  if convert_sentence [i] == 'i' and convert_sentence [i - 1] == ' ' and convert_sentence [i + 1] == ' ':
    convert_sentence[i] = 'I'


final_sentence = ''.join(convert_sentence)
print(final_sentence)


#All thw letters are set to uppercaase to be converted to morse code.
words = final_sentence.upper()




#for loop to convert all the characters to morse code and put these conversions in the new_sentence list.
for i in range(len(final_sentence)):
  for w in range(len(characters)):
    if characters[w] == words[i]:
      new_sentence.insert(INDEX, morse_code[w])
      
  INDEX += 1




#All of the morse code is now printed and separated by spaces
print(' ')
print('Your sentence in morse code is: ')
newer_sentence = ' '.join(new_sentence)
print(newer_sentence)