def booth_rental(income,fee):
    s= [0] * (len(income)+1)
    max_profit = 0
    for i in range(len(income)):
        s[i+1] = s[i] + income[i]
        max_profit = max(max_profit, income[i]-fee, s[i+1]-(i+1)*fee)
    for j in range(1,len(s)-1):
        for k in range(j+1,len(s)-1):
            max_profit = max(max_profit,(s[k]-s[j-1])-(k-j+1)*fee)
    if max_profit == 0:
        return "No"
    else:
        return max_profit
fee = int(input())
income = list(map(int,input().split()))
print(booth_rental(income,fee))

'''
def booth_rental(income, fee):
    n = len(income)
    max_profit = 0
    curr_profit = 0
    
    for i in range(n):
        curr_profit = max(0, curr_profit) + income[i] - fee
        max_profit = max(max_profit, curr_profit)
    
    if max_profit == 0:
        return "No"
    else:
        return max_profit

income = list(map(int, input().split()))
fee = int(input())
print(booth_rental(income, fee))
'''

