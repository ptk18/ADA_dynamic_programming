'''op = {1:'+',2:'*',3:'*'}
memo = {0:0}
def opt(n):
    if n in memo:
        return memo[n]
    else:
        res = 1
        min_op = float('inf')
        for i in op.keys():
            if n >= i:
                res = eval(str(res) + op[i] + str(i))
                min_op = min(min_op, opt(n-res)+1)
        memo[n] = min_op
        return memo[n]
    
print(opt(6))'''

def opt(n):
    memo = {1: 0}
    for i in range(2, n + 1):
        min_ops = float('inf')
        if i % 2 == 0:
            min_ops = min(min_ops, memo[i // 2] + 1)
        if i % 3 == 0:
            min_ops = min(min_ops, memo[i // 3] + 1)
        min_ops = min(min_ops, memo[i - 1] + 1)
        memo[i] = min_ops
    return memo[n]

x = int(input())
print(opt(x))
