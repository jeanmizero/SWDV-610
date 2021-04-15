def insertion_sort(nums):
    for i in range(len(nums)):
        # check each item
        j = i
        # Check the previous item
        while j > 0 and nums[j - 1] < nums[j]:  # descending order
            # keep pushing to the left
            # swap the item
            nums[j - 1], nums[j] = nums[j], nums[j - 1]

            j = j - 1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
insertion_sort(nums)
print("Insertion sorted list:", nums)
