# Merge Sort


# def mergeSort(arr, left, right):
#     if right > left:
#         mid = (right + left) // 2

#         mergeSort(arr, left, mid) #left part
#         mergeSort(arr, mid + 1, right) # right part

#         merge(arr, left, mid, right)


# def merge(arr, left, mid, right):
#     i = left, j = mid + 1, k = 0

#     tmp = [0] * (right - left + 1)

#     while i <= mid and j <= right:
#         if arr[i] < arr[j]:
#             tmp[k] = arr[i]
#             i += 1
#         else:
#             tmp[k] = arr[j]
#             j += 1

#         k += 1

#     while i <= mid:
#         tmp[k] = arr[i]
#         i += 1
#         k += 1

#     while j <= right:
#         tmp[k] = arr[j]
#         j += 1
#         k += 1

#     p = left

#     for x in tmp:
#         arr[p] = x
#         p += 1



























def mergeSort(arr, left, right):
    print("Function call " + str(left) + " " + str(right))

    if right > left:
        mid = (left + right) // 2

        print("Left sub-array call " + str(left) + " " + str(mid))

        # left
        mergeSort(arr, left, mid)

        print("Right sub-array call " + str(mid + 1) + " " + str(right))

        # right
        mergeSort(arr, mid + 1, right)

        print("Merge two sub-array call " + str(left) + " " + str(mid) + " " + str(mid + 1) + " " + str(right))

        # merge two sorted halves
        merge(arr, left, mid, right)

# arr[left...mid], arr[mid + 1...right]
# arr[left...right]

def merge(arr, left, mid, right):
    temp = [0] * (right - left + 1) # sorted arr

    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    print("Temp arr ", temp)

    for idx in range(left, right + 1):
        arr[idx] = temp[idx - left]

# arr = [5, 7, 3, 10, 6, 2]

arr = [6, 5, 12, 10, 9, 1]

mergeSort(arr, 0, len(arr) - 1)

print(arr)
