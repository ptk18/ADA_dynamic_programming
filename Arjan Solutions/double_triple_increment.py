x = int(input())
memo = [0 for _ in range(x+1)]
memo[1]=0

for i in range(2,x+1):
    p = [memo[i-1]]
    if i%2 == 0:
        p.append(memo[i//2])
    if i%3 == 0:
        p.append(memo[i//3])
    memo[i] = min(p)+1

print(memo[x])
    

