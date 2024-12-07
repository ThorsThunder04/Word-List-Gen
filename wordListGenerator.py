"""
Written entirely by Thor.N

This program will generate a word list to use in password cracking.
You will input the characters you want in the word list and the minimum and maximum length of each word.
"""
from itertools import product
#TODO: code the function to calculate all combinations myself. Avoid using recursion if possible

tempnumlist = '1234567890'


print("""
This program will generate a word list file that you will name before the words are generated.
If you already have a wordlist with the same name in the working directory, it will be overridden.
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
        print('Sorry you must enter a whole positive number')
        input('Press Enter to try again...')
        continue
    
    break



while True:
    # gets custom file name (wordlist.txt by default)
    print("\nInput what you wan't to call the file (include extention)")
    customeFileName = input("(Default: wordlist.txt) >> ").strip() or "wordlist.txt"
    
    # make sure all characters for the file name are valid file name characters
    if any([c in customeFileName for c in ("/", "\\", "|", "?", "\"", "'", "<", ">", "*", ":")]):
        print("\nInvalid filename, a file name can't contain any of these characters:")
        print("\, /, |, ?, \", <, >, *, :")
        input("\nPress Enter to try again...")
        continue
    break



total_bytes = 0 # how many bytes will be in the file
total_lines = 0 # how many lines will be in the file

for length in range(min_length, max_length+1):
    totalCombsForLen = len(characters) ** length 

    total_bytes += totalCombsForLen * (length + 2) # +1 because we count newlines too (\n)
    total_lines += totalCombsForLen

# displays the size of the file.
bytes_str = str(total_bytes)
nByteUnits = lambda num, k: (num//(2**(10*k)))%(2**10)

if total_bytes > 0: #displays Bytes
    print("\nYour wordlist file will be :")
    print(nByteUnits(total_bytes, 0), "Bytes")

if total_bytes >= 2**(10*1): #displays KB
    print(nByteUnits(total_bytes, 1), "KB")
    
if total_bytes >= 2**(10*2) : #displays MB
    print(nByteUnits(total_bytes, 2), "MB")

if total_bytes >= 2**(10*3): #displays GB
    print(nByteUnits(total_bytes, 3), "GB")

if total_bytes >= 2**(10*4): #displays TB
    print(nByteUnits(total_bytes, 4), "TB")

if total_bytes >= 2**(10*5): # displays PB
    print(nByteUnits(total_bytes, 5), "PB")

print("\n" + str(total_lines) + " lines will be generated.")

# asks user if they are sure that they want to generate the file
while True:
    answer = input("\nWould you like to continue? [Y/n]>> ").strip().lower() or "y"
    if answer in ["y", "n"]:
        if answer == "y":
            break
        elif answer == "n":
            exit(0)
    else:
        print("\nInvalid Answer: type either y or n to choose")
        input("\nPress Enter to try again...")



#will add each word to the file
with open(customeFileName, 'w') as wordlist:

    #iterates through each length
    for length in range(min_length, max_length + 1):
        prod = list(product(characters, repeat=length))
        for i in range(len(prod)):
            word = "".join(prod[i])
            wordlist.write(word + ("\n" if i < len(prod)-1 else ""))
            print(word)

input("\nPress Enter to exit...")