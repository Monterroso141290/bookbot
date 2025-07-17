import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        text_content = f.read()
    return text_content

def sort_on(dict_list):
    return dict_list["num"]
    

def main():

    

    from stats import book_word_count
    book_content = get_book_text(sys.argv[1])
    print(book_content)
    count = book_word_count(book_content)
    print(count)

    from stats import character_count
    dictionary_count = character_count(book_content)
    print(dictionary_count)

    from stats import sort_characters
    sorted_dictionaries = sort_characters(dictionary_count)
    sorted_dictionaries.sort(reverse=True, key=sort_on)
    print(sorted_dictionaries)

    from stats import print_report
    print_report(count, sorted_dictionaries)


main()