from os import remove


name="AdityaPratapSingh"
vowel=["a","e","i","o","u"]
vlist=[]
clist=[]
c=0
v=0
for i in name:
    if i.lower() in vowel:
        vlist.append(i)
        v=v+1
    else:
        clist.append(i)
        c=c+1
print("Total no of vowel is:",v)
print(vlist)
print("Total no of consonant is:",c)
print(clist)