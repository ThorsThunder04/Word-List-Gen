"""
Written entirely by Thor.N

This program will generate a word list to use in password cracking.
You will input the characters you want in the word list and the minimum and maximum length of each word.
"""

tempnumlist = '1234567890'

pause = lambda: input('\nPress Enter to continue...')

print("""
This program will generate a word list file "wordlist.txt".
IF you already have a wordlist.txt in the working directory, it will be overridden.
""")

#gets list of characters that will be interated through later on
characters = set(input('Enter the characters you want included in the wordlist: '))


#gets max and min lengths of the words and makes sure they are integers.
while True:

    min_length = input('Enter the minimum length you want your words to be (default is 1): ')
    max_length = input('Enter the maximum length you want your words to be: ')
    if (len(min_length) == 0):
        min_length = 1
    
    try:
        min_length = int(min_length)
        max_length = int(max_length)
    except ValueError:
        print('Sorry you must enter a valid number.')
        input('Press Enter to try again...')
        continue
    
    break

#will add each word to the file
with open('wordlist.txt', 'w') as wordlist:
    pass