# Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

def make_dict(keys,values):
    dict1=dict()
    for i in range(len(keys)):
        dict1.update({keys[i]:values[i]})
    return dict1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dicts_obj1=make_dict(keys,values)
print(dicts_obj1)