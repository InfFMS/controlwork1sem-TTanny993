x= 125**5+25**9-30
t=''
while x!=0:
    t= t+str (x%5)
    x=x//5
t= t[::-1]
print(t.count("4"))