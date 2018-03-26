a = [310,285,179,625,351,423,861,254,450,520]
b = [0]*len(a)
def mergesort(_self,l,h):
    if(l<h):
        mid = (l+h)/2
        mergesort(l,mid)
        mergesort(mid+1,h)
        merge(l,mid,h)
    else :
        return
def merge(_self,low,mid,high):
    h=low
    i=low
    j=mid+1
    while((h<=mid) and (j<=high)):
        if(a[h]<=a[j]):
          b[i]=a[j]
          j=j+1
        else:
            b[i]=a[h]
            h=h+1
    if(h>mid):
        for k in range(j,high):
            b[i]=a[k]
            i=i+1
    else:
        for k in range(h,mid):
            b[i]=a[k]
            i=i+1
    for k in range(low,high):
        a[k]=b[k]

mergesort(0,len(a))
for i in range(0,len(a)):
    print(a[i])
