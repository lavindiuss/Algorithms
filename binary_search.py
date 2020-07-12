
def search(arr,l,r,x):
    """
    algorithm = binary search
    arr = array
    l - left subarray of array
    r - right subarray of array
    x - search key
    complexity = O(log n) 
    """

    if r >= l:
        mid = l +(r-1) // 2

        if arr[mid] == x:
            return mid 
        
        elif arr[mid] > x:
            return search(arr, l, mid-1, x) 

        else :
            return search(arr,mid+1,r,x)
    
    else:
        return -1

    
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
