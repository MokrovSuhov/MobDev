def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
    krt = []
    nekrt = []
    for i in range(len(nums)):
        c = 0
        if nums[i] % 3 == 0:
            krt.append(nums[i])
        else:
            nekrt.append(nums[i])
    return krt + nekrt


if __name__ == "__main__":
    # Verify it works
    print("Input:")
    n = int(input())
    array = list(map(int, input().split(' ')))
    srt = bubble_sort(array)
    print('Output', srt)