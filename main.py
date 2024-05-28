import string


def count_the_words(text):
    total = 0
    for line in text:
        line = line.rstrip()
        words = line.split()
        total += len(words)
    return total


def count_the_letters(text):
    letters = list(string.ascii_lowercase)
    letters_dict = dict()
    for line in text:
        line = line.rstrip().lower()
        for char in line:
            if char in letters:
                try:
                    letters_dict[char] += 1
                except:
                    letters_dict[char] = 1
    letters_dict = {k: v for k, v in sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)}
    return letters_dict


def print_report(words_count, letters_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print()
    for key, value in letters_count.items():
        print(f"The '{key}' character was found {value} times"),
    print("--- End report ---")


def main():
    with open("/home/berk/workspace/github.com/BerkAkipek/bookbot/books/frankenstein.txt") as f:
        content = f.read()
        words_count = count_the_words(content)
        letter_count = count_the_letters(content)
        print_report(words_count=words_count, letters_count=letter_count)


if __name__ == '__main__':
    main()
