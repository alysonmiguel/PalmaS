N = int(input())
M = int(input())
vb = []
vp = []
vs = []
for i in range(N):
   vb.append(int(input()))
for i in range(M):
    vp.append(int(input()))
for i in range(M-1):
    if(i != M-2):   
        if(vp[i] > vp[i+1]):
            pi = vp[i]
            pf = vp[i+1]
            for j in range(pi-1, pf-1, -1):
                vs.append(vb[j])
        else:
            pi = vp[i]
            pf = vp[i + 1]
            for j in range(pi - 1, pf - 1):
                vs.append(vb[j])
    else:
        if (vp[i] > vp[i + 1]):
            pi = vp[i]
            pf = vp[i + 1]
            for j in range(pi - 1, pf - 1, -1):
                vs.append(vb[j])
        else:
            pi = vp[i]
            pf = vp[i + 1]
            for j in range(pi - 1, pf):
                vs.append(vb[j])

print(vs.count(0),vs.count(1),vs.count(2),vs.count(3),vs.count(4),vs.count(5),vs.count(6),vs.count(7),vs.count(8),vs.count(9),)
