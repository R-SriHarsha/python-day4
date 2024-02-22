#write a python program to print the sum of maximum and minimum element in a matrix using tuple
l=[]
maxi=0
mini=100000
r,c=map(int,input().split())
for i in range(r):
    t=tuple(map(int,input().split()))
    l.append(t)

print(tuple(l))
for i in l:
    if mini>min(i):
        mini=min(i)
    if maxi<max(i):
        maxi=max(i)
    
print(mini)
print(maxi)
