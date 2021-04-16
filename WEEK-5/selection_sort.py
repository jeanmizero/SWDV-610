def selection_sort(list_value):
    for i in range(0, len(list_value) - 1):
        # Find the minimum value from list by using linear search
        minimum_value = i
        # Find the new smallest value
        for j in range(i + 1, len(list_value)):
            if list_value[j] < minimum_value:  # use ascending order
                minimum_value = j
        # Swap the minimum value with the left-most value and do not swap the value with itself
        if minimum_value != i:
            list_value[i], list_value[minimum_value] = list_value[minimum_value], list_value[i]


list_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selection_sort(list_value)
print("Selection sorted list:", list_value)
