def check(s):
    winning_possibility = "No"
    if len(s) < 2:
        winning_possibility = "Yes"
    elif len(s) >= 2 and (abs(s[0]-s[1]) <= 9 or abs(s[0]-s[-1]) <= 9):
        winning_possibility = "Yes"
        s = s[:1]
        return check(s)
    elif len(s) >= 2 and (abs(s[-1]-s[0]) <= 9 or abs(s[-1]-s[-2]) <= 9):
        winning_possibility = "Yes"
        s.pop()
        return check(s)
    else:
        winning_possibility = "No"
    return winning_possibility

s = list(map(int,input().split()))
print(check(s))
