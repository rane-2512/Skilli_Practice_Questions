def secondLargest(nums: List[int]) -> int:
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)

    if len(unique_nums) < 2:
        return -1

    return unique_nums[1]
