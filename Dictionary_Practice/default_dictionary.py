# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# Expected output:
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 
#  'Emma': {'designation': 'Developer', 'salary': 8000}}


def default_dicts(employees,defaults):
    result = dict.fromkeys(employees,defaults)
    return result
    


employees = ['Kelly', 'Emma']
defaults = {'emp1_data':{"designation": 'Developer', "salary": 8000}} 

obj1=default_dicts(employees,defaults)
print(obj1)
