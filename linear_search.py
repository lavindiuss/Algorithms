


def search(arr,x):
    """
    here we use linear search algorithm to get x index from our array
    arr = array 
    x = our search key
    algorithm complexity = O(n)
    """
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i 
    return -1 

arr = [ 2, 3, 4, 10, 40 ]
x = 10 
result = search(arr,x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result); 