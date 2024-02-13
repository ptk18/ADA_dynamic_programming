def f(x):
    return x * x + x

def opt(y):
    if y <= 0:
        return 0
    lo = 0
    hi = y
    while lo <= hi:
        mid = (lo + hi) // 2
        if f(mid) == y:
            return mid
        elif f(mid) <= y:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

y = int(input())
print(opt(y))
