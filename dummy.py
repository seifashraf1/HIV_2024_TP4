def divide_list(lst):
    n = len(lst)
    size = n // 3  # Calculate the size of each part
    parts = [lst[i * size:(i + 1) * size] for i in range(3)]  # Divide the list into three parts
    return parts

# Example list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Divide the list into three parts
divided_list = divide_list(my_list)

# Print the divided parts
for i, part in enumerate(divided_list, 1):
    print(f"Part {i}: {part}")
