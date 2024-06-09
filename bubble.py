def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped:
            break

    return arr


arr =[3,45,6,7,12,78,90,91]
sorted = bubblesort(arr)
print("Sorted of bubble sorted array: ", sorted)