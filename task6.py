u=1
n=1
for i in range (2,13):
    n=n+2**(u-1)
    u=u+n
print(n)