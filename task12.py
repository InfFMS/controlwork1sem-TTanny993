def rt(n):
    tt=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            tt.append(i)
            if i!=n//i:
                tt.append(n//i)
    return tt

def M(N):
    tt= rt(N)
    tt.sort(reverse=True)
    if len(tt) >= 5:
        return tt[4]
    else:
        return 0

N = 300000001
rr=[]
while len(rr)<5:
    m_value=M(N)
    if m_value>0:
        rr.append((N,m_value))
    N += 1
for n, m in rr:
    print(n,m)