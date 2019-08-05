# ASCII Table

LOWER_VALUE = 33
UPPER_VALUE = 127

# character to number
def chgord():
    # Request a character from user
    userchar = input("Enter a character:")
    # change from character to UTF-8 integer using ord() funtion
    print("The ASCII code for {} is {}".format(userchar,ord(userchar)))

# number to character
def chgchr():
    # Request a integer from user
    usernum = int(input("Enter a number between 33 and 127:"))
    # if user input number is between 33 and 127 , ask again and again
    while usernum < LOWER_VALUE or usernum > UPPER_VALUE:
        usernum = int(input("Enter a number between 33 and 127:"))

    # change from integer to UTF-8 character using chr() function
    print("The character for {} is {}".format(usernum, chr(usernum)))

# all row, customize column
def column():
    columns = int(input("How many cols :"))
    curr = 0
    for i in range(LOWER_VALUE,UPPER_VALUE+1):
        curr += 1
        print("{:3d} {:1s}".format(i,chr(i)),end='|')
        if curr == columns:
            print()
            curr = 0
        i+=1

# customize row
def customize():
    rows = int(input("How many rows :"))
    for j in range(LOWER_VALUE,rows+34):
        print("{:3d} {:1s}".format(j,chr(j)))
        j+=1

# chgord()
# chgchr()
column()
#customize()