P = {1:30,2:40,3:120,4:130,5:150}
memo_profit = {1:P[1]}
memo_cuts = {1:[]}
def opt(n):
    if n in memo_profit:
        return (memo_profit[n],memo_cuts[n])
    else:
        max_profit = P[n]
        max_cuts = None
        for k in range(1,n-1):
            (profit_nk, cuts_nk) = opt(n-k)
            if max_profit < P[k] + profit_nk - k*10:
                max_profit = P[k] + profit_nk - k*10
                max_cuts = [k] + profit_nk[n-k]
            memo_profit[n] = max_profit
            memo_cuts[n] = max_cuts
            return (memo_profit[n], memo_cuts[n])
            
    