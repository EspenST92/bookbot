def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    words = get_num_words(text)
    letters = count_letters(text)
    sorted_letters = sort(letters)
    print_result(book_path, words, sorted_letters)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    lower_case = text.lower()
    letter_dictionary = {}
    for letter in lower_case:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
    return letter_dictionary


def sort(unsorted_dict):
    ordered_dict = {}
    for l in sorted(unsorted_dict, key=unsorted_dict.get, reverse=True):
        if l.isalpha():
            ordered_dict[l] = unsorted_dict[l]
    return ordered_dict


def print_result(book, words, letters):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()
    for l in letters:
        print(f"The '{l}' character was found {letters[l]} times")
    print("--- End report ---")

main()
