S = {1:3,2:7,3:5,4:1,5:4}
def check(k,Y):
    if k == 0:
        return Y == 0
    else:
        if Y >= S[k]:
            return check(k-1,Y) or check(k-1,Y-S[k])
        else:
            return check(k-1,Y)

memo = {}        
def check_memo(k,Y):
    if k == 0:
        return Y == 0
    else:
        if (k,Y) in memo:
            return memo[(k,Y)]
        elif Y >= S[k]:
            memo[(k,Y)] = check(k-1,Y) or check(k-1,Y-S[k])
            return memo[(k,Y)]
        else:
            memo[(k,Y)] = check(k-1,Y)
            return memo[(k,Y)]
            
print(check_memo(5,6))