def quick_sort(A,lo,hi):
    if lo >= hi:
        return
    else:
        pivot_index = select_pivot(A,lo,hi)
        mid1, mid2 = partition(A,lo,hi,pivot_index)
        quick_sort(A,lo,mid1-1)
        quick_sort(A,mid2+1,hi)
        
def partition(A,lo,hi,pivot_index):
    pivot_item = A[pivot_index]
    mid1, mid2 = lo, hi
    i = lo
    while i <= mid2:
        if A[i] < pivot_item:
            A[mid1], A[i] = A[i], A[mid1]
            mid1+=1
            i += 1
        elif A[i] > pivot_item:
            A[mid2], A[i] = A[i], A[mid2]
            mid2 -= 1
        else:
            i+=1
    return mid1, mid2

def select_pivot(A,lo,hi):
    return (lo+hi)//2

A = [3, 6, 8, 10, 1, 2, 1]
quick_sort(A, 0, len(A) - 1)
print(A)