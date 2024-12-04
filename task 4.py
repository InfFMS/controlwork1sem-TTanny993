for x in range (1, 2031):
    n = 3 ** 100 - x
    t=''
    while n!=0:
        t= t+str (n%3)
        n=n//3
        t= t[::-1]
        p=t.count("0")
        if int(p)==2:
            print(x)