"""
Written entirely by Thor.N

This program will generate a word list to use in password cracking.
You will input the characters you want in the word list and the minimum and maximum length of each word.
"""
from itertools import product
#TODO: code the function to calculate all combinations myself. Avoid using recursion if possible


print("""
This program will generate a wordlist file containing all possible combinations of characters you in put
in a range of lengths that you also input. Then the words are outputed to a file.
""")

#gets list of characters that will be interated through later on
characters = set(input("Type the characters to be included in the words: "))


#gets max and min lengths of the words and makes sure they are integers.
while True:

    min_length = input("Enter minimum word length (Default: 1): ") or "1"
    max_length = input("Enter max word length: ") or min_length
    
    try: # make sure they are valid whole numbers
        min_length = int(min_length)
        max_length = int(max_length)
    except ValueError:
        print('Sorry you must enter a whole positive number')
        input('Press Enter to try again...')
        continue
    
    if min_length > max_length:
        print("Error: the minimum length must be smaller or equal to the maximum length")
        input("Press enter to try again...")
        continue
    
    break



while True:
    # gets custom file name (wordlist.txt by default)
    print("\nEnter output file name")
    customeFileName = input("(Default: wordlist.txt): ").strip() or "wordlist.txt"
    
    # make sure all characters for the file name are valid file name characters
    if any([c in customeFileName for c in ("/", "\\", "|", "?", "\"", "'", "<", ">", "*", ":")]):
        print("\nInvalid filename, a file name can't contain any of these characters:")
        print("\, /, |, ?, \", ', <, >, *, :")
        input("\nPress Enter to try again...")
        continue
    break



total_bytes = 0 # how many bytes will be in the file
total_lines = 0 # how many lines will be in the file

for length in range(min_length, max_length+1):
    totalCombsForLen = len(characters) ** length

    total_bytes += totalCombsForLen * (length + 2) - 2 # +2 because we also count newlines and vertical tab ,-2 because on the last line there is no newline or vertical tab
    total_lines += totalCombsForLen

# displays the size of the file.
i = 0
units = ["Bytes", "KB", "MB", "GB", "TP", "PB"]
print("\nYour wordlist file size will be :")
while total_bytes > 0 and i <= 5:
    nUnitBytes = total_bytes % 2**(10)
    if nUnitBytes > 0:
        total_bytes //= 2**(10)
        print(nUnitBytes, units[i])
    i += 1


print(str(total_lines) + " lines will be generated.")

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