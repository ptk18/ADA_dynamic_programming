def g(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        print(f"{g(n-1)} + {g(n-2)} = {g(n-1)+g(n-2)}")
        return g(n-1)+g(n-2)

memo = {0:1, 1:2}   
def g_memo(n):
    if n in memo:
        return memo[n]
    else:
        print(f"{g_memo(n-1)} + {g_memo(n-2)} = {g_memo(n-1)+g_memo(n-2)}")
        memo[n] = g_memo(n-1)+g_memo(n-2)
        return memo[n] 
    
memo2 = [1,2]
def g_memo2(n):
    if n < len(memo2):
        return memo2[n]
    else:
        memo2.append(g_memo2(n-1) + g_memo2(n-2))
        return memo2[n]  
    
def g_bottom_up(N):
    g = [0] * (N+1)
    g[0], g[1] = 1,2
    for i in range(2,N+1):
        g[i] = g[i-1] + g[i-2]
        print(i, g[i])
    return g[N]

def best_ver(N):
    if N==0:
        return 1
    if N==1:
        return 2
    else:
        k = 2
        g2, g1 = 1, 2
        while k <= N:
            k = k+1
            print(g2,g1)
            g2, g1 = g1, (g1+g2)
        return g1 
       
print(g_bottom_up(20))
print(best_ver(20))