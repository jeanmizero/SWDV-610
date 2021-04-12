def bubble_sort(list_value):
    index_length = len(list_value)
    # Traverse through all array elements
    for i in range(index_length):
        # Last i elements are already in place
        for j in range(0, index_length - i - 1):
            # Swap if the element found is greater han the next element
            # Use descending order
            if list_value[j] < list_value[j + 1]:
                list_value[j], list_value[j +
                                          1] = list_value[j + 1], list_value[j]


list_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bubble_sort(list_value)
print("Bubble sorted list:", list_value)
