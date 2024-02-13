def min_cost_cutting(l, cuts):
    n = len(cuts)
    cuts = [0] + cuts + [l] 
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    for length in range(2, n + 2):
        for start in range(n + 2 - length):
            end = start + length
            min_cost = float('inf')
            for k in range(start + 1, end):
                min_cost = min(min_cost, dp[start][k] + dp[k][end])
            dp[start][end] = cuts[end] - cuts[start] + min_cost

    return dp[0][n + 1]

l = int(input())
cuts = list(map(int,input().split()))
print(min_cost_cutting(l,cuts))

