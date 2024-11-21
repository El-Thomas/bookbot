def main() :
    char_list = []
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    number_of_words = count_words(text)
    characters = count_characters(text)

    for char, count in characters.items():
        char_dict = {
            "name" : char,
            "num" : count
        }
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_dictionary)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in {book_path}.\n")
    
    for char_dict in char_list:
        print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")

    print("--- End report ---")
       

def open_book(book) :
    with open(book) as f:
        return f.read()

def count_words(words)  :
    words = words.split()
    return len(words)

def count_characters(book):
    book = book.lower()  
    characters = {
        'a' : book.count("a"),
        'b' : book.count("b"),
        'c' : book.count("c"),
        'd' : book.count("d"),
        'e' : book.count("e"),
        'f' : book.count("f"),
        'g' : book.count("g"),
        'h' : book.count("h"),
        'i' : book.count("i"),
        'j' : book.count("j"),
        'k' : book.count("k"),
        'l' : book.count("l"),
        'm' : book.count("m"),
        'n' : book.count("n"),
        'o' : book.count("o"),
        'p' : book.count("p"),
        'q' : book.count("q"),
        'r' : book.count("r"),
        's' : book.count("s"),
        't' : book.count("t"),
        'u' : book.count("u"),
        'v' : book.count("v"),
        'w' : book.count("w"),
        'x' : book.count("x"),
        'y' : book.count("y"),
        'z' : book.count("z")
    }
    
    return characters

def sort_dictionary(dict) :
    return dict["num"]


main()