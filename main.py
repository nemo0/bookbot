def get_word_count(data):
    return len(data.split())


def letter_counter(data):
    lowercased = data.lower()
    words = lowercased.split()

    counts = {}
    for word in words:
        for letter in word:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

    return counts


with open("./books/frankenstein.txt") as file:
    data = file.read()
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{get_word_count(data)} words found in the document\n")
    letters_counts = letter_counter(data)

    for letter, count in letters_counts.items():
        print(f"The '{letter}' character was found {count} times")
