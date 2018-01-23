# -*- coding: utf-8 -*-
"""
堆排序

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
"""


def heapify(arr, i, length):
    """
    堆调整
    """
    left = 2 * i + 1  # 左孩子节点
    right = 2 * i + 2  # 右孩子节点
    largest = i

    if left < length and arr[left] > arr[largest]:
        largest = left

    if right < length and arr[right] > arr[largest]:
        largest = right

    if (largest != i):
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, length)


def build_max_heap(arr):
    """
    构建大顶堆
    """
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i, len(arr))

    return arr


def heap_sort(arr):
    """
    堆排序

    算法说明
    -----
    1. 将初始待排序关键字序列 (R1,R2....Rn) 构建成大顶堆，此堆为初始的无序区；
    2. 将堆顶元素 R[1] 与最后一个元素 R[n] 交换，此时得到新的无序区 (R1,R2,......Rn-1) 
       和新的有序区 (Rn),且满足 R[1,2...n-1]<=R[n]；
    3. 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区 (R1,R2,......Rn-1) 调整为新堆，
       然后再次将 R[1] 与无序区最后一个元素交换，
       得到新的无序区 (R1,R2....Rn-2) 和新的有序区(Rn-1,Rn)。
       不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。
    """
    arr = build_max_heap(arr)
    length = len(arr)

    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        length -= 1
        heapify(arr, 0, length)

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = heap_sort(arr)
    print(result)
