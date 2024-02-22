#write a python program to print the sum of even palindromes in a range and also print the list of even palindromes
'''
def palindrome(i):
    s=str(i)
    l=len(s)
    if s==s[::-1]:
            return True
    return False
        
        
        


l1=[]
l2=[]
n,m=map(int,input().split())

for i in range(n,m+1):
    
    if palindrome(i):
            
        l2.append(i)
        if i%2==0:
            
            l1.append(i)
        
print(l2)
print(l1)
print(sum(l1))
'''





def palindrome(i):
    s=str(i)
    l=len(s)
    if s==s[::-1]:
            return True
    return False
        
        
        


l1=[]
l2=[]
n,m=map(int,input().split())

for i in range(n,m+1):
    
    if palindrome(i):
            
        l2.append(i)
        if i%2==0:
            
            l1.append(i)
        
print(l2)
print(l1)
print(sum(l1))


















