# -*- coding: utf-8 -*-
"""
快速排序
"""


def partition(arr, left, right):
    """
    分区
    """
    pivot = left  # 设定基准值
    index = pivot + 1

    for i in range(index, right + 1):
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1

    arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]

    return index - 1


def quick_sort(arr, left=0, right=0):
    length = len(arr)
    left = 0 if type(left) != int else left
    right = length - 1 if type(right) != int else right

    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = quick_sort(arr)
    print(result)
