def square_odd_numbers(numbers):
    l1=[]
    # Your code here
    for i in numbers:
        if i%2!=0:
            l1.append(i*i)
    return l1
            


# Example usage:
numbers = [1, 2, 3, 4, 5]
print(square_odd_numbers(numbers))  # Output should be [1, 9, 25]
