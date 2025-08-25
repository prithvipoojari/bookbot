def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def count_words(filepath):
    book_text = get_book_text(filepath)
    number_of_words = 0
    list_book_text = book_text.split()
    for text in list_book_text:
        number_of_words += 1
    return number_of_words
    
def count_of_characters(filepath):
    book_text = get_book_text(filepath)
    number_of_characters = {}
    lowercase_book_text = book_text.lower()
    list_book_text = lowercase_book_text.split()

    for text in list_book_text:
        for character in text:
            if character.isalpha():
                if character in number_of_characters:
                    number_of_characters[character] += 1
                else:
                    number_of_characters[character] = 1
    return number_of_characters
def sort_on(item_dictionary):

    return item_dictionary["num"]

def sorted_list_of_dictionaries(filepath):
    number_of_characters_currentfunc = count_of_characters(filepath)
    sorted_list_of_dict = []
    for key in number_of_characters_currentfunc:
        sorted_list_of_dict.append({"char": key, "num": number_of_characters_currentfunc[key]})
    sorted_list_of_dict.sort(reverse=True, key=sort_on)
    return sorted_list_of_dict