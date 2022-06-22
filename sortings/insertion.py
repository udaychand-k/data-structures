"""
This type of insertion sort uses while loop and coping of adjacent elements
"""

a=list ( map( int, list(input('enter elements: ').split())))
n= len( a) # insertion sort
for i in range ( 1,n):
    temp=a[ i]
    j=i-1
    while j>=0 and a[ j]>temp:
        a [ j+1]=a[ j]
        j=j-1
    a[ j+1]=temp
print( a)

"""
This type of insertion sort uses for loops with swapping of adjacent elements
"""

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
