def selectionSort(li):
    size = len(li)
    for i in range(0, size - 1):
        min_ind = i
        for j in range(i + 1, size)