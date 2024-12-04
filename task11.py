def rt(r,t):
    for number in range(r,t+1):
        tt= []
        for rr in range(2, int(number**0.5) + 1):
            if number % rr == 0:
                tt.append(rr)
                if tt != number // rr:
                    tt.append(number//rr)
        if len(tt)==2:
            tt.sort()
            print(tt[0],tt[1])
rt(174457, 174505)