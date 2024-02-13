a = float(input())
b = float(input())
c = float(input())
 
max_r = 0.0
max_profit = 0.0
for r100 in range(1,2001):
    r = r100/100
    profit = a*(r*r*r)+b*(r*r)+c*r
    if profit > max_profit:
        max_profit = profit
        max_r = r
    
print(round(max_r, 2))
