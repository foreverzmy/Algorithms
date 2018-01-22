# -*- coding: utf-8 -*-
"""
堆排序
"""


def heapify(arr, i):
    """
    堆调整
    """
    length = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < length and arr[left] > arr[largest]:
        largest = left

    if right < length and arr[right] > arr[largest]:
        largest = right

    if(largest != i):
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest)


def build_max_heap(arr):
    """
    构建大顶堆
    """
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)

    return arr


def heap_sort(arr):
    arr = build_max_heap(arr)
    length = len(arr)

    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        length -= 1
        heapify(arr, 0)

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = heap_sort(arr)
    print(result)
