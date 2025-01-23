def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    word_dict = get_char_num(text)
    sort_by_size(word_dict)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_num(text):
    unique_letters = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter.isalpha():
            if letter in unique_letters:
                unique_letters[letter] += 1
            else:
                unique_letters.update({letter: 1})

    return unique_letters

def sort_on(dict):
    return dict["num"]

def sort_by_size(dict):
    list_of_letters = []
    for key in dict:
        list_of_letters.append({"letter": key, "num": dict[key]})

    list_of_letters.sort(reverse=True, key=sort_on)

    for element in list_of_letters:
        print(f"The '{element['letter']}' character was found {element['num']} times")

main()
