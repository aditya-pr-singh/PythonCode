list1=[22,33,44,56,67,90]
new_list=[]
for i in list1:
    if i not in (22,33):
        new_list.append(i)
print(new_list)