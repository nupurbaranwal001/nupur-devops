def bubbleSort(arr):
    lst = arr
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


a = [1, 11, 2, -1, 3, 55, 22, 33]
b = bubbleSort(a)
print("Output with a sorted list {}" .format(b))

