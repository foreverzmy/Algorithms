"""
插入排序
"""


def insertion_sort_up(arr):
    """
    从小到大排序
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


def insertion_sort_down(arr):
    """
    从大到小排序
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


arr = [5, 2, 4, 6, 1, 3]
result_up = insertion_sort_up(arr)
print(result_up)
result_down = insertion_sort_down(arr)
print(result_down)