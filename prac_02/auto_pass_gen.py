import random

ALPHABET = "abcdefghijclmnpqrstuvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
DIGIT = "123456789"
min_length = int(input("Enter Minimum Length"))
max_length = int(input("Enter Maximum Length"))

digit = input("Digit Required (Y)es or (N)o")
digit_required = False
if digit.lower() == "y":
    digit_required = True

special_chars = input("Special Chars Required (Y)es or (N)o")
special_chars_required = False
if special_chars.lower() == "y":
    special_chars_required = True

def generator(digit_required,special_chars_required,min_length,max_length):
    word = ""
    length = random.randint(min_length, max_length)
    print("Length:",length)

    for i in range(length):
        opt = random.randint(1, 3)
        print("Option:",opt)
        if opt == 1:
            word += random.choice(ALPHABET)
        elif opt == 2:
            if digit_required:
               word += random.choice(DIGIT)
            elif special_chars_required:
                word += random.choice(SPECIAL_CHARACTERS)
            else:
                word += random.choice(ALPHABET)
        elif opt==3 and special_chars_required:
            word += random.choice(SPECIAL_CHARACTERS)
    print(word,end='')

generator(digit_required,special_chars_required,min_length,max_length)
max