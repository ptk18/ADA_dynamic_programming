y = int(input())
lo = 0
hi = y

while lo <= hi:
    mid = (hi+lo)//2
    z = mid*mid+mid
    if z == y:
        x = mid
        break
    elif z < y:
        x = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(x)
