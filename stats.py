def book_word_count(book_text):
    text = book_text
    words = text.split()
    word_amount = len(words)
    final_message = f"{word_amount} words found in the document"
    return word_amount

def character_count(book_text):
    total_count = {}
    lower_book_text = book_text.lower()
    for char in lower_book_text:
        if char in total_count:
            total_count[char] += 1
        else:
            total_count[char] = 1
    return total_count

def sort_characters(total_count):
    dict_list = []
    for character in total_count:
        new_dict = {"char": character, "num": total_count[character]}
        dict_list.append(new_dict)
    return dict_list

def print_report(word_count, sorted_dictionary):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_dictionary:
        if char["char"].isalpha():
            print (f'{char["char"]}: {char["num"]}')
    print("============= END ===============")

