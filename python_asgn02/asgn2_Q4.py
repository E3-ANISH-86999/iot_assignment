def enter_list(list_len:int):
    list1 = []
    i = 0
    while i < list_len:
        list1.append(input(f"Enter word at {i}'th pos: "))
        i += 1
    return list1


def find_longest_word(list2):
    max_len = 0
    for word in list2:
        word_len = len(word)
        if max_len < word_len:
            max_len = word_len
    
    return max_len


word_list = enter_list(5)

max = find_longest_word(word_list)
print(f"Lenght of longest word outof {word_list} is: {max} ")

