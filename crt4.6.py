#write a python program to print sum of elements in the last column in a matrix
l=[]
sums=0
r,c=map(int,input().split())
for i in range(r):
    t=tuple(map(int,input().split()))
    sums+=t[c-1]
    l.append(t)
print(tuple(l))
print("sum of elments in last column:",sums)
