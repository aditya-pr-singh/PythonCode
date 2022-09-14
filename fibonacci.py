# def fab(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     return fab(n-1) + fab(n-2)

# for i in range(100,101):
#     print(i,fab(i))



def fab(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return fab(n-1) + fab(n-2)

for i in range(100,101):
    print(i,fab(i))



