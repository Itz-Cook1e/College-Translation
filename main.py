# Assignment:
# Write a Dictionary that converts English numbers to French, one through five. (That would be un, deux, trois, quatre, cinq.) 
# Ask for user input for an English number, and output the French one. Print a nice error message if the text entered isn't in the dictionary. 
# Hint, there is am example in the book that is almost like this. Another hint, this should take 6 lines of code.

translations = {'one':'une', 'two':'deux', 'three':'trois', 'four':'quatre', 'five':'cinq'}

english_word = input('Please enter a number one - five (spelt out): ')

if english_word not in translations:
    print(f'{english_word} is not a number one - five.')
else:
    print(f'{english_word} is {translations[english_word]} in French!')


# Comment with name, date, and assignment name redacted
