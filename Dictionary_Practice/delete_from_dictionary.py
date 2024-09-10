# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# ------------------Do your code below-----------------
def delete_from_dict(keys,sample_dict):
    for key in keys:
        sample_dict.pop(key)
    return(sample_dict)
    

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]


obj1=delete_from_dict(keys,sample_dict)
print(obj1)