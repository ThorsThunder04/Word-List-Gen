"""
Written entirely by Thor.N

This program will generate a word list to use in password cracking.
You will input the characters you want in the word list and the minimum and maximum length of each word.
"""
from itertools import product

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


#makes the length iterable
ranged_length_limit = list(range(min_length, max_length+1))


#calculates how big the text file will be.
total_bytes = 0
for length in ranged_length_limit:
    total_bytes += len(characters) ** (length) * (length + 2)

if total_bytes >= 1000 and total_bytes < 1000000:
    print("\nYour wordlist file will be " + str(total_bytes)[:-3] + "." + str(total_bytes)[-3:-1] + " KB")
elif total_bytes >= 1000000 and total_bytes < 10**9:
    print("\nYour wordlist file will be " + str(total_bytes)[:-6] + '.' + str(total_bytes)[-6:-5] + " MB")
elif total_bytes >= 10**9 and total_bytes < 10**12:
    print("\nYour wordlist file will be " + str(total_bytes)[:-9] + "." + str(total_bytes)[-9:-7] + " GB")
elif total_bytes >= 10**12 and total_bytes < 10**15:
    print("\nYour wordlist file will be " + str(total_bytes)[-12] + "." + str(total_bytes)[-12:-10] + " TB")

while True:
    print("\nWould you like to continue?")
    answer = input("y for yes, n for no >> ")
    if answer == "y":
        break
    elif answer == "n":
        exit()



#will add each word to the file
with open('wordlist.txt', 'w') as wordlist:

    generated_words = 0

    #iteratese through each length
    for length in ranged_length_limit:
        for word in product(characters, repeat=length):
            wordlist.write(''.join(word) + "\n")
            generated_words += 1
            print(''.join(word))

input("\nPress Enter to exit...")