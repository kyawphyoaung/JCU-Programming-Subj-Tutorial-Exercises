def main():
    words = []
    word = input("Enters the words: ")
    words.append(word)
    while word:
        if not word:
            break
        word = input("Enters the words: ")
        words.append(word)
    words.sort()
    seen = set()
    seen_twice = set(x for x in words if x in seen or seen.add(x))
    # print(words)
    # print(seen_twice)
    if not seen_twice:
        print("No repeated strings entered")
    else:
        count =0
        for word in seen_twice:
            print("Strings repeated: {}".format(list(seen_twice)[count]))
            count +=1

main()