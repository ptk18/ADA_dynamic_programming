def enough(capa):
    avail = capa
    for i in range(len(stations)-1):
        dist = stations[i+1]-stations[i]
        if dist<=avail:
            avail -= dist
        elif dist<=capa-1:
            capa -= 1
            avail = capa-dist
        else:
            return False
    return True

d = int(input())
stations = [int(x) for x in input().split()]
input()

# Add location of home at the beginning and location of office at the end
stations.insert(0,0)
stations.append(d)

hi = d
lo = 1
least = hi
while lo<=hi:
    mid = (lo+hi)//2
    if enough(mid):
        least = min(least,mid)
        hi = mid-1
    else:
        lo = mid+1
        
print(least)

