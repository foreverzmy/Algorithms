# -*- coding: utf-8 -*-
"""
计数排序

计数排序(Counting sort)是一种稳定的排序算法。计数排序使用一个额外的数组 C，其中第 i 个元素是待排序数组 A 中值等于 i 的元素的个数。然后根据数组 C 来将 A 中的元素排到正确的位置。它只能对整数进行排序。
"""


def counting_sort(arr):
    """
    计数排序

    算法说明
    -------
    1. 找出待排序的数组中最大和最小的元素；
    2. 统计数组中每个值为 i 的元素出现的次数，存入数组 C 的第 i 项；
    3. 对所有的计数累加（从 C 中的第一个元素开始，每一项和前一项相加）；
    4. 反向填充目标数组：将每个元素 i 放在新数组的第 C(i) 项，每放一个元素就将 C(i) 减去1。
    """
    bucket = [0 for i in range(max(arr) + 1)]
    length = len(arr)

    # 遍历计算元素个数
    for i in range(length):
        bucket[arr[i]] += 1

    sort_index = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            arr[sort_index] = j
            sort_index += 1
            bucket[j] -= 1

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = counting_sort(arr)
    print(result)
