a=list(map(int,input('enter : ').split()))
n=len(a)
for i in range(1,n):
    key=a[i]
    for  j in range(i,0,-1):
        if a[j]<a[j-1]:
            #swapping the members of array
            a[j],a[j-1]=a[j-1],a[j]
        else:
            #a[j]=key
            break 
    
print(a)