def f(x):
    return x**3+3*x+10

def solve_seq(lo,hi,ys):
    for x in range(lo,hi+1):
        print(x,f(x))
        if f(x)==ys:
            return x
        elif f(x)>ys:
            break
    return None
print(solve_seq(0,100,658774))