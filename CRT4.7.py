#write a python program to print addition of two matrices
r,c=map(int,input().split())
l1=[]
l2=[]
print("input matrix 1:")
print("")

for i in range(r):
    t1=tuple(map(int,input().split()))
    l1.append(t1)
print("input matrix 2:")
print("")
for j in range(r):
    t2=tuple(map(int,input().split()))
    l2.append(t2)

tu1=tuple(l1)
tu2=tuple(l2)

print("matrix1:",tu1)
print("matrix2:",tu2)

l3=[]
for k in range(r):
    list3=[]
    for l in range(c):
        list3.append(l1[k][l]+l2[k][l])
    l3.append(tuple(list3))

print("matrix after addition",tuple(l3))


