def get_num_words(book_text):
    word_count = book_text.split()
    return len(word_count)

def get_text_count(character_text):
    character_count_text = character_text.lower()
    count_dict = {}
    
    for char in character_count_text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sort_on(character_counter):
    return character_counter["num"]

def sort_counts(count_dict):
    char_list = []
    for char, count in count_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list