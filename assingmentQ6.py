def kthSmallest(arr, n, k): 
  
    
    arr.sort() 
 
    return arr[k-1] 
  
if __name__=='__main__': 
    arr = [7,10,4,3,20,15] 
    n = len(arr) 
    k = 3
    print("K'th smallest element is", 
          kthSmallest(arr, n, k)) 