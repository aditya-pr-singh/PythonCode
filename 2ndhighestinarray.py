from os import remove


num=[12,13,14,15,34,56,87,23,90,45]
max1=num[0]
max2=num[1]
for i in num:
    if(max1<i):
        max1=i
print(max1)
num.remove(max1)
for i in num:
    if(max2<i):
        max2=i
print(max2)