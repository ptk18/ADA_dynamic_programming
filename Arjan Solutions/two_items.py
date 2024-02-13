
def binsearch(items, lo, hi, x):
    while lo<=hi:
        mid = (lo+hi)//2
        if items[mid]==x:
            return mid
        elif x<items[mid]:
            hi = mid-1
        else:
            lo = mid+1
    return None

m = int(input())
items = [int(x) for x in input().split()]
items.sort()
k = len(items)-1
m2 = m//2

found = False
while k>0 and items[k]>=m2:
    y = binsearch(items, 0, k-1, m-items[k])
    if y is not None:
        print("Yes")
        found = True
        break
    k-=1

if not found:
    print("No")







