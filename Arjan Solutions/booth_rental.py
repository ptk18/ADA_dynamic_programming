def kadane(p):
    cur_sum = 0
    max_sum = 0
    for x in p:
        cur_sum += x
        if cur_sum < 0:
            cur_sum = 0
        max_sum = max(max_sum, cur_sum)
    return max_sum

fee = int(input())
income_list = [int(i) for i in input().split()]
profit_list = [i-fee for i in income_list]

max_profit = kadane(profit_list)

if max_profit>0:
    print(max_profit)
else:
    print("No")
