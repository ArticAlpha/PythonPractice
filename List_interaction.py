def list_interaction(l1,l2):
    set1=set(l1)
    set2=set(l2)

    interaction = set1.intersection(set2)
    return list(interaction)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

li=list_interaction(list1,list2)
print(li)