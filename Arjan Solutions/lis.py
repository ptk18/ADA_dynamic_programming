p =[int(x) for x in input().split()]
p.insert(0,0)

opt = [0 for _ in p]
for i in range(1,len(opt)):
    r = [opt[j] for j in range(1, i) if p[j]<=p[i]]
    r.append(0)
    opt[i] = max(r)+1

print(max(opt))


