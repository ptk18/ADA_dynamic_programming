C = {1:1, 2:2, 3:4, 4:5}
memo = {0:0}
def opt(n):
    if n in memo:
        return memo[n]
    else:
        min_stamp = float('inf')
        for t in range(1, len(C) +1):
            if n >= C[t]:
                min_stamp = min(min_stamp, opt(n - C[t])+ 1)
        memo[n] = min_stamp
        return memo[n]
    
def opt_bt(m):
    op = [0] * (m+1)
    op[0] = 0
    for n in range(1,m+1):
        min_stamp = float('inf')
        for t in range(1,len(C)+1):
            if n >= C[t]:
                min_stamp = min(min_stamp, op[n-C[t]] + 1)
            op[n] = min_stamp
    return op[m]
        
print(opt(7))
print(opt_bt(7))