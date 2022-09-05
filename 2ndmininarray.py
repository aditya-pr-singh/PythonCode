num=[99,0,12,13,14,15,34,56,87,23,90,45]
min1=num[0]
min2=num[1]
for i in num:
    if(min1>i):
        min1=i
num.remove(min1)
for i in num:
    if(min2>i):
        min2=i
print(min2)