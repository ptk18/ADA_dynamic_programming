def binsearch_rec(A,lo,hi,x):
    if hi < lo:
        return None
    else:
        mid = (lo+hi)//2
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            return binsearch_rec(A,lo,mid-1,x)
        else:
            return binsearch_rec(A,mid+1,hi,x)
        
def binsearch(A,lo,hi,x):
    while lo <= hi:
        mid = (lo+hi)//2
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            hi = mid-1
        else:
            lo = mid+1
    return None

def binsearch_first(A,lo,hi,x):
    result = 0
    while lo <= hi:
        mid = (lo+hi)//2
        if x == A[mid]:
            result = mid
            hi = mid-1
        elif x < A[mid]:
            hi = mid-1
        else:
            lo = mid+1
    return result

def binsearch_last(A,lo,hi,x):
    result = None
    while lo <= hi:
        mid = (lo+hi)//2
        if x == A[mid]:
            result = mid
            lo = mid+1
        elif x < A[mid]:
            hi = mid-1
        else:
            lo = mid+1
    return result

def binsearch_closet(A,lo,hi,x):
    closet_below = None
    closet_above = None
    while lo<=hi:
        mid = (lo+hi)//2
        if x == A[mid]:
            return (mid,mid)
        elif x < A[mid]:
            closet_above = mid
            hi = mid-1
        else:
            closet_below = mid
            lo = mid+1
    return (closet_below,closet_above)
        
A = [1,2,3,4,5,6]
print(binsearch_rec(A,0,len(A)-1,5))
print(binsearch(A,0,len(A)-1,5))

B = [1,2,3,5,5,5,6,7,8]
print(binsearch_first(B,0,len(B)-1,5))
print(binsearch_last(B,0,len(B)-1,5))
print(binsearch_closet(B,0,len(B)-1,4))
