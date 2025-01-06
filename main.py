def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_count_in_text(text)
    characters_in_text = character_dict(text)
    print(text)
    print(f"There are {word_count} words in this text.")
    print(f"This is the character count in this text: \n-----\n{characters_in_text}\n-----")
    
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

main()