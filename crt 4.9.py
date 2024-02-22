#print the count of the vowels and list of the vowels in each word in a sentence
'''
def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i.lower() in "aeiou"
            vc+=1
            s1+=1
    print("Vowel count:",vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)
            




'''


def vowcount(i,l):
    vow={'a','e','i','o','u'}
    count=0
    for j in i:
        if j in vow:
            count+=1
            l.append(j)
            
    return count


s=list(map(str,input("enter a sentence:").split()))
print("number of vowels and list of vowels in each word:")
c=0
for i in s:
    l=[]
    c=vowcount(i,l)
    print("vowel count:",c)
    print("vowels:",list(set(l)))
