# -*- coding: utf-8 -*-
"""
希尔排序

希尔排序是插入排序的一种更高效率的实现。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。
"""


def shell_sort(arr):
    """
    希尔排序

    算法说明
    -------
    1. 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
    2. 按增量序列个数k，对序列进行 k 趟排序；
    3. 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
    """
    length = len(arr)
    gap = 1

    while gap < length / 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, length):
            temp = arr[i]
            for j in range(i, 0, -gap):
                if temp < arr[j - gap]:
                    arr[j] = arr[j - gap]
                else:
                    j += gap
                    break
                arr[j - gap] = temp
        gap //= 3

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = shell_sort(arr)
    print(result)
