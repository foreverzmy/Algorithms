# -*- coding: utf-8 -*-
"""
桶排序

桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排
"""
from insertion_sort import insertion_sort


def bucket_sort(arr, bucket_size=10):
    """
    桶排序

    算法说明
    1. 设置一个定量的数组当作空桶；
    2. 遍历输入数据，并且把数据一个一个放到对应的桶里去；
    3. 对每个不是空的桶进行排序；
    4. 从不是空的桶里把排好序的数据拼接起来。
    """
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)

    # 桶的初始化
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for i in range(bucket_count)]

    # 利用映射函数将数据分配到各个桶中
    for i in range(len(arr)):
        buckets[(arr[i] - min_value) // bucket_size].append(arr[i])

    arr = []
    for i in range(len(buckets)):
        insertion_sort(buckets[i])
        for j in range(len(buckets[i])):
            arr.append(buckets[i][j])

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = bucket_sort(arr)
    print(result)
