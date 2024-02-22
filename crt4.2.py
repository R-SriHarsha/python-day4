#write a python program to print sum of the given matrix
r,c=map(int,input().split())
l=[]
s=0
for i in range(r):
    l.append(list(map(int,input().split(" "))))

for i in l:
    s+=sum(i)
print(l)
print(s)
