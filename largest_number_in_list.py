def largest_number(list1):
    largest_number=0
    for i in list1:
        if largest_number<i:
            largest_number=i
    return largest_number
        
num_list=[23,45,55,30]
a=largest_number(num_list)
print(a)