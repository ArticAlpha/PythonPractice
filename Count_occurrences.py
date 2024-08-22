def count_occurerance(list,element):
    count=0
    for i in list:
        if i==element:
            count+=1
    return count

count1=count_occurerance([1,2,2,2,33,22,2,3],2)
print(count1)