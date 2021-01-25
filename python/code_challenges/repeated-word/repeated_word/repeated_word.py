def repeated_word(string):
    # separate the string
    string = string.split(' ')
    separated_string = []
    for word in string:
        if word not in separated_string:
            separated_string.append(word)
    for word in range(0, len(separated_string)):
        print(separated_string[word], 'appears',
              string.count(separated_string[word]))


def main():
    string = "mercedes mercedes mexico orange spoon orange gary gary"
    repeated_word(string)


if __name__ == "__main__":
    main()
