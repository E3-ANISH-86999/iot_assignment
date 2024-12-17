def enter_list(list_len:int):
    list1 = []
    i = 0
    while i < list_len:
        list1.append(int(input(f"Enter value at {i}'th pos: ")))
        i += 1
    return list1


def max_num(list2):
    max = 0
    for i in list2:
        if max < i:
            max = i
    
    return max


num_list = enter_list(5)

max = max_num(num_list)
print(f"Max of {num_list} is: {max} ")

