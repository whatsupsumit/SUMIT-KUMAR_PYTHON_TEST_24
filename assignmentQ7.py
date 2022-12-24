def countpairs(x,length,sum):
    count = 0
    for i in range(0,length):
       for j in range(i+1,length):
            print(x[i],x[j])   
            if(x[i]+x[j]==sum):
                count+=1
    print(count)


x  = [1,5,7,-1]
sum =6
length=len(x)
countpairs(x,length,sum)