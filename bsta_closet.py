def f(x):
    return x**3 + 3*x + 10

def solve_seq(lo,hi,ys):
    for x in range(lo, hi+1):
        if f(x) == ys:
            return x
        elif f(x) > ys:
            break
    return None

def solve_bin(lo,hi,ys):
    while lo<=hi:
        mid = (lo+hi)//2
        y = f(mid)
        if ys == y:
            return mid
        elif ys < y:
            hi = mid-1
        else:
            lo = mid+1
    return None

def solve_bin_closet(lo,hi,ys):
    closet_below = None
    closet_above = None
    while lo<=hi:
        mid = (lo+hi)//2
        y = f(mid)
        print(mid,y)
        if ys == y:
            return closet_below
        elif ys < y:
            closet_above = mid
            hi = mid-1
        else:
            closet_below = mid
            lo = mid+1
    return (closet_below,closet_above)

def solve_bin_closet_epsilon(lo,hi,epsilon,ys):
    closet_below = None
    while lo<=hi:
        mid = round((lo+hi)/2,2)
        y = round(f(mid),2)
        print(mid,y)
        if ys == y:
            return closet_below
        elif ys < y:
            hi = mid - epsilon
        else:
            closet_below = mid
            hi = mid + epsilon
    return closet_below

print(solve_bin_closet(0,100,658774))

#print(solve_bin_closet_epsilon(0.0,10.0,0.01,15.18))