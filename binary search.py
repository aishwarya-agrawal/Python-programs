import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index
li=[5,6,9,12,10001,563300,456231,789,56234,415263,8526,7456,6325,5412,454]
find = input()
print(bin_search(li,int(find)))
