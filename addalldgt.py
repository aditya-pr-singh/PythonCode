# num=12345
# num2=0
# for i in str(num):
#     num2=num2+int(i)
# print(num2)


num=34567
sum=0
while(num>0):
    dgt=num%10
    sum=sum + dgt
    num=num//10
print(sum)