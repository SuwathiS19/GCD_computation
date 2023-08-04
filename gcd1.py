def gcd(a,b):
    m=[]
    i=0
    for i in range(1,min(a,b)+1):
        if(a%i)==0 and (b%i)==0:
            m.append(i)
    return(m[-1])
c=gcd(120,7)
print(c)
