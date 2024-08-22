def remove_duplicates(lst):
    list1=set(lst)
    return sorted(list(list1))

# Example usage:
lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))  # Output should be [1, 2, 3, 4, 5]
