def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_count_in_text(text)
    characters_in_text = character_dict(text)
    report(book_path, word_count, characters_in_text )
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count_in_text(text):
    words = text.split()
    return len(words)

def character_dict(text):
    text = text.lower()
    alphabet_dict = {}
    for char in text:
        if char not in alphabet_dict:
            alphabet_dict[char] = 1
        else:
            alphabet_dict[char] += 1
    
    return alphabet_dict

def report (book_path, word_count, characters_in_text):
    print(f"---- Begin report of {book_path} ----")
    print(f"{word_count} words found in the text \n")

    for char in characters_in_text:
        if char.isalpha():
            print(f"The {[char]} was found {characters_in_text[char]} times")

    print("\n---- End Report ----")
main()