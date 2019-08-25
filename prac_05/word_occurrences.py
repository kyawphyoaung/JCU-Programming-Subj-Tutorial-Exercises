"""
Do-from-scratch Exercises
Word occurrences program by Kyaw Phyo Aung (13822414)

Copy this text to test :
this is a collection of words of nice words this is a fun thing it is

"""

word_to_count = {}
words = []
words_list = []


def main():
    text = input("Text: ")
    words.append(text.split(" "))
    words_list = words[0]
    # print(words)
    # print(words_list)
    for word in words_list:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    # print(word_to_count)

    # sort the key in word_to_count dictionary
    # print all counted words
    for word in sorted(word_to_count.keys()):
        # align the number
        print("{:10s} : {:2d}".format(word, word_to_count[word]))


main()
