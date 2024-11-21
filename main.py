def main() :
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    number_of_words = count_words(text)
    number_of_characters = count_characters(text)
    
    print(f"{number_of_words} words found in {book_path}.")
    print(f"{number_of_characters} characters found in {book_path}")

def open_book(book) :
    with open(book) as f:
        return f.read()

def count_words(words)  :
    words = words.split()
    return len(words)

def count_characters(book):
    book.lower()  
    characters = {
        'a' : book.find("a"),
        'b' : book.find("b"),
        'c' : book.find("c"),
        'd' : book.find("d"),
        'e' : book.find("e"),
        'f' : book.find("f"),
        'g' : book.find("g"),
        'h' : book.find("h"),
        'i' : book.find("i"),
        'j' : book.find("j"),
        'k' : book.find("k"),
        'l' : book.find("l"),
        'm' : book.find("m"),
        'n' : book.find("n"),
        'o' : book.find("o"),
        'p' : book.find("p"),
        'q' : book.find("q"),
        'r' : book.find("r"),
        's' : book.find("s"),
        't' : book.find("t"),
        'u' : book.find("u"),
        'v' : book.find("v"),
        'w' : book.find("w"),
        'x' : book.find("x"),
        'y' : book.find("y"),
        'z' : book.find("z")
    }
    
    return characters


main()