"""
Written entirely by Thor.N

This program will generate a word list to use in password cracking.
You will input the characters you want in the word list and the minimum and maximum length of each word.
"""
from itertools import product

tempnumlist = '1234567890'

pause = lambda: input('\nPress Enter to continue...')

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
        print('Sorry you must enter a valid number.')
        input('Press Enter to try again...')
        continue
    
    break


#makes the length iterable
ranged_length_limit = list(range(min_length, max_length+1))

while True:
    #gets custom file name. (wordlist.txt by default)
    print("\nInput what you wan't to call the file (include extention)")
    customeFileName = input("(Default: wordlist.txt) >> ")
    if len(customeFileName) == 0:
        customeFileName = "wordlist.txt"
    
    #Makes sure the characters can be used in the file name.
    if "/" in customeFileName or "\\" in customeFileName or ":" in customeFileName or "*" in customeFileName or "?" in customeFileName or "'" in customeFileName or "<" in customeFileName or ">" in customeFileName or "|" in customeFileName:
        print("\nThat file name is not valid, it can't contain the following:")
        print("\, /, |, ?, \", <, >, *, :")
        input("\nPress Enter to try again...")
        continue
    break
"""            
    for letter in customeFileName:
        for sign in ["/", "\\", "|", "<", ">", "*", ":"]:
            if letter == sign:
                print("\nThat file name is no valid, it can't contain the following:")
                print("\, /, |, ?, \", <, >, *, :")
                input("\nPress Enter to try again...")
                break
        
    break
"""


#calculates how big the text file will be. Also how many words will be generated.
total_bytes = 0
total_lines = 0
for length in ranged_length_limit:
    total_bytes += len(characters) ** (length) * (length + 2)

    total_lines += len(characters) ** length

#displays the size of the file.
iter_bytes = str(total_bytes)[::-1]
if total_bytes > 0 and total_bytes < 1000: #displays up to Bytes
    print("\nYour wordlist file will be :")
    print(iter_bytes, "Bytes")

elif total_bytes >= 1000 and total_bytes < 1000000: #displays up to KB
    print("\nYour wordlist file will be :")
    print(iter_bytes[:3], "Bytes")
    print(iter_bytes[3:], "KB")
    
elif total_bytes >= 1000000 and total_bytes < 10**9: #displays up to MB
    print("\nYour wordlist file will be :")
    print(iter_bytes[:3], "Bytes")
    print(iter_bytes[3:6], "KB")
    print(iter_bytes[6:], "MB")

elif total_bytes >= 10**9 and total_bytes < 10**12: #displays up to GB
    print("\nYour wordlist file will be :")
    print(iter_bytes[:3], "Bytes")
    print(iter_bytes[3:6], "KB")
    print(iter_bytes[6:9], "MB")
    print(iter_bytes[9:], "GB")

elif total_bytes >= 10**12 and total_bytes < 10**15: #displays up to TB
    print("\nYour wordlist file will be :")
    print(iter_bytes[:3], "Bytes")
    print(iter_bytes[3:6], "KB")
    print(iter_bytes[6:9], "MB")
    print(iter_bytes[9:12], "GB")
    print(iter_bytes[12:], "TB")

elif total_bytes >= 10**15 and total_bytes < 10**18: # displays up to PB
    print("\nYour wordlist file will be :")
    print(iter_bytes[:3], "Bytes")
    print(iter_bytes[3:6], "KB")
    print(iter_bytes[6:9], "MB")
    print(iter_bytes[9:12], "GB")
    print(iter_bytes[12:15], "TB")
    print(iter_bytes[15:], "PB")

print("\n", total_lines, "lines will be generated.")

while True:
    print("\nWould you like to continue?")
    answer = input("y for yes, n for no >> ")
    if answer == "y":
        break
    elif answer == "n":
        exit()



#will add each word to the file
with open(customeFileName, 'w') as wordlist:

    generated_words = 0

    #iteratese through each length
    for length in ranged_length_limit:
        for word in product(characters, repeat=length):
            wordlist.write(''.join(word) + "\n")
            generated_words += 1
            print(''.join(word))

input("\nPress Enter to exit...")