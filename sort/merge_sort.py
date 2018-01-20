"""
归并排序
"""
import math


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)

    if right:
        result.extend(right)

    return result


def merge_sort(arr):
    length = len(arr)
    if length < 2:
        return arr

    middle = math.floor(length / 2)
    left = arr[:middle]
    right = arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


arr = [8, 2, 5, 7, 4, 6, 3, 4, 1]

result = merge_sort(arr)
print(result)
