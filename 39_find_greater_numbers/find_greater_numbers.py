def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    if num[1] > num[0]:
        add 1 total
        go to the next one
    if num[2] > num[0]
        add 1 total
        go to the next one
    else:
        start over (return or break?)
    
    if num[2] > num[1]:
        add 1 total
        go to the next one
    if num[3] > num[1]


    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    total = 0

    for num in nums:
        for i in range(len(nums)):
            if i > nums.index(num):
                if nums[i] > num:
                    total += 1
    return total