memo = {}
def check(k, y):
  if k == 0:
    return y==0
  else:
    if (k, y) in memo:
      return memo[(k, y)]
    elif y >= s[k]:
      memo[(k, y)] = check(k-1, y) or check(k-1, y-s[k])
      return memo[(k, y)]
    else:
      memo[(k, y)] = check(k-1, y)
      return memo[(k, y)]
 
s = [int(x) for x in input().split()]
y = int(input())
s.insert(0,0)
print(check(len(s)-1, y))
