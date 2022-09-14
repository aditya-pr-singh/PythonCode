# arr1=[1,2,3,4,5,6,7]
# for i in range(len(arr1)):
#     if(i>i+1)or(i<i+1):
        
#     else:
#         print("not monotonic")

def ismonotonnic(A): 
    count=0
    for i in range(len(A)):
        if(i>i+1)or(i<i+1):
            count=count+1
    if count!=0:
        print("monotonic array")
A=[1,2,3,4,5,6,7]
ismonotonnic(A)