def filereadwrite():
    username = input("Enter your name :")
    namefile = open('data.txt','w')

    # Write user input name to data.txt file
    namefile.write(username)
    namefile.close()

    # Check write process achieve or not
    print("Write Success!")

    filedata = open('data.txt','r')

    # readname means get name data from text file
    readname = filedata.read()
    # check read process is achieve or not
    print("Read Success!")
    print("Your name is {}".format(readname))

def numberread():
    # numbefile is a file object of number.txt
    numberfile = open('number.txt', 'r')
    # read numbers from number.txt and add data to num variable
    num = numberfile.readlines()

    # resultnum is for to add numbers which from text file
    resultnum = 0

    for x in num:
        # changing string type to integer
        number = int(x)
        resultnum += number
    print(resultnum)
    numberfile.close()

def fourthblock():
    # numbetwo is the file object of numbertwo.txt
    numbertwo = open('numbertwo.txt', 'r')

    # read numbers from number.txt and add data to numtwo variable
    numtwo = numbertwo.readlines()

    # result is for adding numbers which from text file
    result = 0
    for x in numtwo:
        numbers = int(x)
        result += numbers
    print(result)
    numbertwo.close()

filereadwrite()
numberread()
fourthblock()