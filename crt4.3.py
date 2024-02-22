#product of elements in a matrix
'''
r,c=map(int,input().split())
l=[]
p=1
for i in range(r):
    l.append(list(map(int,input().split(" "))))

for j in l:
    for k in j:
        p*=k
print(p) 
'''
























r,c=map(int,input().split())
l=[]
p=1
for i in range(r):
    l1=[]
    for j in range(c):
        
        k=int(input())
        p*=k
        l1.append(k)
    l.append(l1)


print(l)
print(p)










