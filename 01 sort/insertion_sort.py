# -*- coding: utf-8 -*-
"""
插入排序

插入排序的算法描述是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，
在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序在实现上，通常采用in-place排序（即只需用到 O(1) 的额外空间的排序），
因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
"""


def insertion_sort(arr):
    """
    插入排序

    算法描述
    -------
    1. 从第一个元素开始，该元素可以认为已经被排序；
    2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
    3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
    4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    5. 将新元素插入到该位置后；
    6. 重复步骤2~5。
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


def binary_insertion_sort(arr):
    """
    二分法插入排序

    算法描述
    ------
    1. 将取出的元素与已排序区的中间值比较;
    2. 找出元素所在区间;
    3. 重复以上步骤，直到区间只剩一个大于取出元素的值;
    4. 将取出元素插入到前面;
    """
    for i in range(1, len(arr)):
        key = arr[i]
        left = 0
        right = i - 1

        while left <= right:
            middle = (left + right) // 2  # 取整
            if key < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1

        for j in range(i - 1, left, -1):
            arr[j + 1] = arr[j]

        arr[left] = key

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = insertion_sort(arr)
    print(result)
    result = binary_insertion_sort(arr)
    print(result)
