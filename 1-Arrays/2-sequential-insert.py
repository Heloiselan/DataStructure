"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引
如果目标值不存在于数组中，返回它将会被按顺序插入的位置
"""


def search(nums: list[int], target: int):
    """
    依次比较元素值和目标值
        如果目标值大于所有元素值，则直接插入到最后，返回数组长度+1
        如果目标值等于元素值，返回当前元素的索引
        如果目标值小于元素值，插入至n-1位置，并返回n-1
    """
    for index, num in enumerate(nums):
        if (num >= target):
            return index
    return len(nums)


def searchInsert(nums: list[int], target: int) -> int:
    """
    二分法寻找
    """
    left, right = 0, len(nums)-1

    while left <= right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left


if __name__ == '__main__':
    nums: list = [1, 3, 5, 6]
    target: int = 8
    index = searchInsert(nums, target)
    print(f'插入位置是{index}')
