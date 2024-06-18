"""
给你一个整数数组nums，请计算数组的中心下标

数组中心下标是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和

如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素
这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回最靠近左边的那一个
如果数组不存在中心下标，返回 -1 
"""


def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # all = sum(nums)
    # left_sum = 0
    # for i in range(len(nums)):
    #     if (left_sum * 2 + nums[i] == all):
    #         print("中心下标为：", i)
    #         return i
    #     else:
    #         left_sum += nums[i]
    # print("没有中心下标")
    # return -1

    all = sum(nums)
    left_num = 0
    for i in range(len(nums)):
        all -= nums[i]
        if (left_num == all):
            print("中心下标为：", i)
            return i
        else:
            left_num += nums[i]

    print("没有中心下标")
    return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    nums2 = [1, 2, 3]
    nums3 = [2, 1, -1]
    pivotIndex(nums=nums)
    pivotIndex(nums=nums2)
    pivotIndex(nums=nums3)
