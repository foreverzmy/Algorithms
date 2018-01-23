# -*- coding: utf-8 -*-
"""
基数排序

基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。基数排序基于分别排序，分别收集，所以是稳定的。
"""


def radix_sort(arr):
    """
    基数排序

    算法说明
    -------
    1. 取得数组中的最大数，并取得位数；
    2. arr为原始数组，从最低位开始取每个位组成radix数组；
    3. 对radix进行计数排序（利用计数排序适用于小范围数的特点）；
    """
    length = len(arr)
    if length == 0:
        return arr

    mod = 10
    dev = 1

    buckets = [[] for i in range(10)]

    # 按照个位数分桶
    for i in range(length):
        single = arr[i] % 10
        buckets[single].append(arr[i])

    arr = []
    for i in range(len(buckets)):
        arr += buckets[i]

    buckets = [[] for i in range(10)]
    # 按照十位数分桶
    for i in range(length):
        tens = arr[i] // 10
        buckets[tens].append(arr[i])

    arr = []
    for i in range(len(buckets)):
        arr += buckets[i]

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = radix_sort(arr)
    print(result)
