def quick_sort(array, low, high):
    if (low < high): 
        pivot_pos = partition(array, low, high)
        print("left side of",pivot_pos,array[pivot_pos],array)
        quick_sort(array, low, pivot_pos-1)
        print("Right side of",pivot_pos,array[pivot_pos],array)
        quick_sort(array, pivot_pos+1, high)
        
def partition(array, low, high) :
    pivot = low
    l = low
    h = high
    while(l<h) :
        while l<=h and array[l] <= array[pivot] :
            l = l + 1
        while h>=l and array[h] > array[pivot] :
            h = h - 1
        if l < h :
            swap(array, l, h)
    swap(array, h, pivot)
    return h
def swap(array, ind1, ind2) :
    temp = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = temp
# Driver code
array = [9,7,1,8,4,3,5]
quick_sort(array, 0, len(array) -1)
print(array)