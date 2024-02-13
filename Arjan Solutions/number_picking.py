memo = {}

def onewins(left, right, prev):
    if left==right:
        return abs(game[left]-prev) < 10

    if (left, right, prev) in memo:
        return memo[(left, right, prev)]
    
    if abs(game[left]-prev)<10:
        if onewins(left+1, right, game[left]):
            memo[(left,right,prev)] = True
            return True
        
    if abs(game[right]-prev)<10:
        if onewins(left, right-1, game[right]):
            memo[(left, right, prev)] = True
            return True
        
    memo[(left, right, prev)] = False    
    return False


game = [int(x) for x in input().split()]
n = len(game)

if onewins(1, n-1, game[0]) or onewins(0, n-2, game[n-1]):
    print("Yes")
else:
    print("No")
