def main():
    path = "books/frankenstein.txt"
    


    with open(path) as f:
        file_contents = f.read()
    word_num = word_count(file_contents)
    char_dictionary = count_char(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(char_dictionary)

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item['num']} times")


def word_count(text):
    word_list = text.split()
    count = len(word_list)
    return count

def count_char(text):
    dictionary = {}
    lowercase_list = text.lower()
    for c in lowercase_list:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] +=1
    return dictionary

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]
main()
