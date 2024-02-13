def quick_select(A, lo, hi, i):
    if lo == hi and i == lo:
        return A[i]
    
    pivot_index = select_pivot(A, lo, hi)
    mid1, mid2 = partition(A, lo, hi, pivot_index)
    
    if i < mid1:
        return quick_select(A, lo, mid1 - 1, i)
    elif i > mid2:
        return quick_select(A, mid2 + 1, hi, i)
    else:
        return A[i]

def partition(A, lo, hi, pivot_index):
    pivot_value = A[pivot_index]
    mid1, mid2 = lo, hi
    i = lo
    
    while i <= mid2:
        if A[i] < pivot_value:
            A[mid1], A[i] = A[i], A[mid1]
            mid1 += 1
            i += 1
        elif A[i] > pivot_value:
            A[i], A[mid2] = A[mid2], A[i]
            mid2 -= 1
        else:
            i+=1
    return mid1, mid2

def select_pivot(A, lo, hi):
    return (lo+hi)//2

# Example usage:
A = [18, 32, 15, 23, 9, 14, 31, 28]
k = 4
print("Original List:", A)
result = quick_select(A, 0, len(A) - 1, len(A) - k)  # Finding the kth largest element
print(f"The {k}th largest element is:", result)
