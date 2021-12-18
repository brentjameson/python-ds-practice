def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    nums_length = len(nums)
    x = 0
    i = 1
    while i < nums_length:
        if nums[x] + nums[i] == goal:
            # return (f"{nums}({i}),{nums}({i + 1})")
            return (nums[x], nums[i])
        print(x, 'i am x')
        print(i, 'i am i')

        # INFINITE LOOP BELOW. DON'T TRY IT. JUST FOR REFERENCE
        # if i == nums_length:
        #     i = 1
        #     x += 1
        #     if x == nums_length:
        #         return ()