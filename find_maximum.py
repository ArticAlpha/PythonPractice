def find_max(numbers):
    max=numbers[0]
    # Your code here
    for i in numbers:
        if i>max:
            max=i
    return max

# Example usage:
numbers = [-1,-2,-3,-4]
print(find_max(numbers))  # Output should be 5
