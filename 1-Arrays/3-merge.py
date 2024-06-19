

def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    方法：排序
    """
    intervals.sort(key=lambda x: x[0])  # 集合按左边界排序
    merges = list()  # 合并集合
    for interval in intervals:
        # 如果合并集没有元素
        # 或
        # 新元素的左边界大于合并集尾元素的右边界，表示两个元素没有交集
        # 将当前元素尾端插入至合并集
        if not merges or merges[-1][-1] < interval[0]:
            merges.append(interval)
        # 如果合并集最后一个元素的右边界大于等于当前集合的左边界
        # 合并集最后一个元素的右边界取原值与当前集合的右边界中的较大值
        else:
            merges[-1][-1] = max(merges[-1][-1], interval[1])
    return merges


if __name__ == '__main__':
    test: list = [[1, 3], [2, 6], [8, 10], [15, 18]]
    test2 = [[8, 9], [2, 3], [4, 5], [6, 7]]
    m = merge(test2)
