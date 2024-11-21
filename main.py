def main() :
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    number_of_words = count_words(text)
    print(f"{number_of_words} words found in {book_path}.")

def open_book(book) :
    with open(book) as f:
        return f.read()

def count_words(words)  :
    words = words.split()
    return len(words)


main()