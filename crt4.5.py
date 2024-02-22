#average of matrix
l=[]
sums=0
r,c=map(int,input().split())
for i in range(r):
    t=tuple(map(int,input().split()))
    l.append(t)
    sums+=sum(t)

print(tuple(l))
avg=0
avg=sums/(r*c)
print(sums)
print("avg:",avg)


    
