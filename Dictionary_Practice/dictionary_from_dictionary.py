# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# output
# {'name': 'Kelly', 'salary': 8000}


#----------------------Do your code below----------------
def dict_from_dict(keys,sampleDict):
    new_dict={}
    for key in keys:
        new_dict[key] = sampleDict[key]
    return(new_dict)


sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

obj1=dict_from_dict(keys,sampleDict)
print(obj1)