def count_c_Jeb_words(filename):
    count = 0

    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()

    for word in words:
        if len(word) < 4:
            continue
        if word[0] != "c":
            continue
        if word[-3:] == "Jeb":
            count += 1

    return count