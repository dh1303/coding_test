a,b=map(int,input().split(' '))
c=1
if b<0:
    c=-1
    b=abs(b)
print(a//b*c,a%b,sep='\n')