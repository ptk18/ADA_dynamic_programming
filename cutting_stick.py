P = {1:30,2:40,3:120,4:130,5:150}
def opt(n):
    if n == 1:
        return P(n)
    else:
        max_profit = P[n]
        for k in range(1,n-1):
            max_profit = max(max_profit, P[k] + opt(n-k) - k*10) # C = (k-1)*10
        return max_profit

memo = {1:P[1]}   
def opt_memo(n):
    if n in memo:
        return memo[n]
    else:
        max_profit = P[n]
        for k in range(1,n-1):
            max_profit = max(max_profit, P[k]+opt_memo(n-k)-k*10)
        memo[n] = max_profit
        return memo[n]
    

def opt_bt(N):
    opt = [0] * (N+1)
    opt[1] = P[1]
    for n in range(2, N+1):
        max_profit = P[n]
        for k in range(1, n-1):
            max_profit = max(max_profit, P[k] + opt[n-k] - k*10)
        opt[n] = max_profit
    return opt[N]

    
print(opt(4))
print(opt_memo(5))
print(opt_bt(5))
    