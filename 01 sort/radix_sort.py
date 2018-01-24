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
    2. 遍历数组，从最低位开始取每个位组成 radix 数组；
    3. 将 radix 展开为一维数组；
    4. 重复2，3步，直至最高位也遍历完成，radix 展开的一维数组即为有序数组。
    """
    length = len(arr)
    if length == 0:
        return arr

    level = 1  # 初始化位数为1
    max_value = max(arr)  # 取得数组中最大值
    # 取得位数
    while max_value // 10**level > 0:
        level += 1

    for l in range(1, level + 1):
        buckets = [[] for i in range(10)]

        # 按照位数分桶
        for j in range(length):
            digit = arr[j] % (10**l) // (10**(l - 1))
            buckets[digit].append(arr[j])
        arr = []
        for i in range(len(buckets)):
            arr += buckets[i]

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = radix_sort(arr)
    print(result)
