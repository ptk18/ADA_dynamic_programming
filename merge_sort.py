def merge_sort(P):
    if len(P) <= 1:
        return P
    else:
        M = len(P)//2
        SL = merge_sort(P[:M])
        SR = merge_sort(P[M:])
        return merge(SL,SR)
    
def merge(SL, SR):
    S = []
    i,j = 0,0
    NL, NR = len(SL), len(SR)
    while i < NL or j < NR:
        if i >= NL:
            S.append(SR[j])
            j+=1
        elif j >= NR:
            S.append(SL[i])
            i+=1
        elif SL[i] <= SR[j]:
            S.append(SL[i])
            i+=1
        else:
            S.append(SR[j])
            j+=1
    return S

P = [1,5,7,9,3]
print(merge_sort(P))