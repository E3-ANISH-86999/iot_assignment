def concatenate_list():
    list1 = ["Hello", "take"]
    list2 = ["Dear", "Sir"]
    list3 = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            list3.append(list1[i] + " " + list2[j])
    
    return list3


list4 = concatenate_list()
print(list4)


