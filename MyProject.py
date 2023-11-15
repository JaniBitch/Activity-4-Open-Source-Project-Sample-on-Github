def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

#sample data
data = [12,45,23,67,89,34,56,78,90,32,10,5,39,48,51,92,42,61,73,18,73,88,37,29,84,70,14,96,25,69]

sorted_data = bubble_sort(data)
print("Soryed Data:", sorted_data)