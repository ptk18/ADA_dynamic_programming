memo = {}

def opt(a,b):
    if b <= a+1:
        return 0
    else:
        if (a,b) in memo:
            return memo[(a,b)]
        options = []
        for k in range(a+1,b):
            options.append(opt(a,k)+opt(k,b)+p[b]-p[a])
        memo[(a,b)] = min(options)
        return memo[(a,b)]
            
stick_len = int(input())
p = [int(x) for x in input().split()]
p.insert(0,0)
p.append(stick_len)
print(opt(0,len(p)-1))




