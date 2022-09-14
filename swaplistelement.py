
list1=[1,2,3,4,5]
list1[0],list1[-1]=list1[-1],list1[0]
print(list1)


mylist=[1,2,3,4,5]
mylist2=[1,2]
list3=[]
for i in mylist:
    if i not in mylist2:
        list3.append(i)
print(list3)



# numlist=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for i in numlist:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)