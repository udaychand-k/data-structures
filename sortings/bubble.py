a=list(map(int,input('enter elements by space : ').split()))
n=len(a)
for i in range(n-1):
    for j in range(n-1-i):
        if a[j+1]<a[j]:
            #swapping the adjacent elements
            a[j],a[j+1]=a[j+1],a[j]
print(a)