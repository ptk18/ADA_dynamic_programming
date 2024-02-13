def opt(a, b, c):
    max_profit = 0
    max_interest = 0
    r = 0.00
    while r <= 20.01:
        current_profit = a * (r**3) + b * (r**2) + c * r
        if current_profit > max_profit:
            max_profit = current_profit
            max_interest = r
        r += 0.01
    if max_interest == 0:
        return 0.0
    return round(max_interest,2)

a = float(input())
b = float(input())
c = float(input())
print(opt(a, b, c))
