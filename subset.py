memo = []
def check(s, y):
    if len(s) == 0:
        return y == 0
    elif y in memo:  # Using tuple(s) to make it hashable
        return True
    else:
        if s[-1] <= y:
            result = check(s[:-1], y) or check(s[:-1], y - s[-1])
            memo.append(result)
            return result
        else:
            result = check(s[:-1], y)
            memo.append(result)
            return result

s = list(map(int, input().split()))
y = int(input())
print(check(s, y))
