def rearrangeArray(arr, N):
    ind = None

    for i in range(N):
        if (arr[i] == 0):
            ind = i;
            break;
 
    j = -1
    temp = None
    for k in range(N):
        if (arr[k] < 0):
            j += 1;

            if (arr[j] == 0):
                j += 1;
 
            temp = arr[j];
            arr[j] = arr[k];
            arr[k] = temp;
         
    temp = arr[ind];
    arr[ind] = arr[j];
    arr[j] = temp;
 
    for i in range(N):
        print(arr[i], end=" ");
 

arr = [1, 12, -2, 3, 4, 0,1,2,3,4];
N = len(arr)
 
rearrangeArray(arr, N);