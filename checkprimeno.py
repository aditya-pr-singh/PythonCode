a=23
flag=0
i=2
while(i<a-1):
    if (a%i==0):
        flag=flag+1
        print("no is not prime")
        break
    i=i+1

if(flag==0):
    print('prime no.')