book = "books/frankenstein.txt"

with open(book) as f:
    file_contents = f.read()


def wordCount(text):
    words = text.split()
    return len(words)


def letterCount(text):
    letters = {}
    lowerText = text.lower()
    for char in lowerText:
        if char.isalpha():
            if char not in letters:
                letters[char] = 0
            letters[char] += 1
    return letters


def sortDictionary(unsortedDictionary):
    sortedDictionary = dict(
        sorted(unsortedDictionary.items(), key=lambda x: x[1], reverse=True))
    return sortedDictionary


def report(text):
    print(f"Breakdown Report of {book} :\n")
    print(f"This document contains {wordCount(text)} different words.\n\n")
    sortedDictionary = sortDictionary(letterCount(file_contents))
    for letter in sortedDictionary:
        print(
            f"This document contains {sortedDictionary[letter]} instances of the '{letter}' character.")
    print(f"\n\nEnd of report.")


report(file_contents)
