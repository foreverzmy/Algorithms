"""
选择排序

选择排序是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
"""


def selection_sort(arr):
    """
    冒泡排序-升序

    算法描述
    -------
    1. 初始状态：无序区为R[1..n]，有序区为空;
    2. 第i趟排序 (i=1,2,3...n-1) 开始时，当前有序区和无序区分别为 R[1..i-1] 和 R(i..n）。该趟排序从当前无序区中选出关键字最小的记录 R[k]，将它与无序区的第 1 个记录 R 交换，使 R[1..i] 和 R[i+1..n) 分别变为记录个数增加 1 个的新有序区和记录个数减少 1 个的新无序区;
    3. n-1趟结束，数组有序化了;
    """
    length = len(arr)
    minIndex = 0

    for i in range(0, length - 1):
        minIndex = i

        for j in range(i + 1, length):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 5, 26, 27, 2, 46, 4, 19, 50, 48]
    result = selection_sort(arr)
    print(result)
