# merge 2 dictionaries

def merge_dicts(dict1,dict2):
    dict1.update(dict2)
    return dict1

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict_ob1=merge_dicts(dict1,dict2)
print(dict_ob1)