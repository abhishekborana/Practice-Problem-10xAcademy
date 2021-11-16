def stringInsertionSort(str):
    # Your code goes here
    arr=[]
    for i in str:
    	arr.append(i)
    for i in range(1, len(arr)): 
  
        val = arr[i]
        j = i-1
        while j >=0 and val < arr[j] : 
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=val
    arr="".join(arr)
    return arr
         

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))