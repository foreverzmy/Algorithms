# -*- coding: utf-8 -*-
"""
归并排序

归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

"""
import math


def merge(left, right):
    """
    子序列合并

    说明
    ----
    将两个子序列合并为一个有序子序列
    """
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)

    if right:
        result.extend(right)

    return result


def merge_sort(arr):
    """
    归并排序

    算法说明
    -------
    1. 把长度为n的输入序列分成两个长度为n/2的子序列；
    2. 对这两个子序列分别采用归并排序；
    3. 将两个排序好的子序列合并成一个最终的排序序列。
    """
    length = len(arr)
    if length < 2:
        return arr

    middle = math.floor(length / 2)
    left = arr[:middle]
    right = arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = merge_sort(arr)
    print(result)
