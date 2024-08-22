## Add numbers in a list
def sum_list(list):
    sum=0
    for i in list:
        sum+=i
    return sum

sum1=sum_list([1,2,3])
print(sum1)