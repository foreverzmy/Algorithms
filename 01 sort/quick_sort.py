# -*- coding: utf-8 -*-
"""
快速排序

快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
"""


def partition(arr, left, right):
    """
    分区

    算法说明
    -------
    1. 从数列中挑出一个元素，称为 "基准"（pivot）;
    2. 排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    """
    pivot = left  # 设置基准值
    index = pivot + 1

    for i in range(index, right + 1):
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1

    arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]

    return index - 1


def quick_sort(arr, left=0, right=None):
    """
    快速排序主函数

    算法说明
    -------
    1. 从数列中挑出一个元素，称为 "基准"（pivot）；
    2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    """
    length = len(arr)

    right = length - 1 if type(right) != int else right

    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)

    return arr


def quick_sort2(arr):
    """
    快速排序改进

    算法说明
    -------
    1. 以中间值作为基准，并将其取出;
    2. 遍历数组，将小于基准的数放入左数组，大于基准的数放入右数组;
    3. 递归调用 1，2 两部，直至每个数组的长度不大于 1;
    4. 递归时拼接长度不大于 1 的数组;
    """
    length = len(arr)
    if length <= 1:
        return arr

    pivot_index = length // 2
    pivot = arr.pop(pivot_index)

    left = []
    right = []

    for i in range(0, length - 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort2(left) + [pivot] + quick_sort2(right)


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = quick_sort(arr)
    print(result)
    result = quick_sort2(arr)
    print(result)
