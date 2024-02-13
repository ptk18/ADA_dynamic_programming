'''
def select_items(m, items):
    items.sort()  # Sort in ascending order
    for i in range(len(items)-1):
        x = m - items[i]
        result = binsearch(items, i+1, len(items)-1, x)
        if result == "Yes":
            return "Yes"
    return "No"

def binsearch(my_list, lo, hi, x):
    while lo <= hi:
        mid = (lo + hi) // 2
        if x == my_list[mid]:
            return "Yes"
        elif x < my_list[mid]:  # Adjusting the comparison
            hi = mid - 1
        else:
            lo = mid + 1
    return "No"

m = int(input())
items = list(map(int,input().split()))
print(select_items(m, items))
'''
def select_items(m, items):
    items.sort()
    left, right = 0, len(items) - 1
    
    while left < right:
        total = items[left] + items[right]
        if total == m:
            return "Yes"
        elif total < m:
            left += 1
        else:
            right -= 1
            
    return "No"


m = int(input())
items = list(map(int,input().split()))
print(select_items(m, items))
