"""
冒泡排序

冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
"""
import time


def bubble_sort(arr):
    """
    简单冒泡排序

    算法描述
    -------
    1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个;
    2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数;
    3. 针对所有的元素重复以上的步骤，除了最后一个;
    4. 重复步骤1~3，直到排序完成;
    """
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - 1 - i):
            if arr[j] > arr[j + 1]:  # 相邻元素对比
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 元素交换

    return arr


def bubble_sort2(arr):
    """
    标志位冒泡排序

    说明
    ___
    设置一标志性变量 pos,用于记录每趟排序中最后一次进行交换的位置。
    由于 pos 位置之后的记录均已交换到位,故在进行下一趟排序时只要扫描到pos位置即可
    如果有一趟排序中没有产生交换的话，pos 为 0，那么说明此刻数列以及变成了有序的数列
    """
    i = len(arr) - 1  # 初始时，最后位置保持不变
    while i > 0:
        pos = 0  # 每次循环式，无交换记录
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                pos = j  # 记录交换的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i = pos  # 为下一次排序做准备

    return arr


def bubble_sort3(arr):
    """
    正反冒泡排序

    说明
    ---
    传统冒泡排序中每一趟排序操作只能找到一个最大值或最小值,
    我们考虑利用在每趟排序中进行正向和反向两遍冒泡的方法一次
    可以得到两个最终值(最大者和最小者),从而使排序趟数几乎减少了一半
    """
    low = 0
    high = len(arr) - 1

    while low < high:
        # 正向冒泡，找最大值
        for j in range(low, high):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        high -= 1
        # 反向冒泡，找最小值
        for j in range(high, low, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

        low += 1

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]

    # 方法一
    time_start = time.clock()
    result = bubble_sort(arr)
    time_end = time.clock()
    print(time_end - time_start)

    # 方法二
    time_start = time.clock()
    result = bubble_sort2(arr)
    time_end = time.clock()
    print(time_end - time_start)

    # 方法三
    time_start = time.clock()
    result = bubble_sort3(arr)
    time_end = time.clock()
    print(time_end - time_start)
