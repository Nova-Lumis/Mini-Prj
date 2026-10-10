# Binary search algorithm.
def binary_search(numbers_list, target):
    # Determine total member in numbers_list
    n = len(numbers_list)

    # Determining the left and right variable according to binary search algorithm
    left = 0
    right = n - 1

    times = 0

    while left <= right:
        # Determining how many times the loop triggered
        times += 1

        # Determining the middle part
        middle = left + int(((right - left) // 1) / 2)

        # Checking value
        if numbers_list[middle] < target:
            left = middle + 1
        elif numbers_list[middle] > target:
            right = middle - 1
        else:
            display = f"Number of times it takes to get result: {times}\n"
            display += f"The target {target} found in the list at index {middle}, with value {numbers_list[middle]}."
            return display
        
        
    # If the target isn't found in the list
    return "Unsuccessfull"


# Main testing 
list_testing = [3, 37, 67, 90, 24, 66, 89, 99, 100]
list_testing.sort()
print(list_testing)
print(binary_search(list_testing, 89))
