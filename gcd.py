a=raw_input()
a=a.split()
c=raw_input()
c=c.split()
b=int(a[1])
f=[]
def fungcd(a,b):
    if(b==0):
        return a
    else:
        return fungcd(b,a%b)

for i in range(0,b):
    d=raw_input()
    d=d.split()
    x=int(d[0])
    y=int(d[1])
    g=(fungcd(x,y))
    for g in c:
        print(g)
        break
    
