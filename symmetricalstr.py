s=input("Enter a string:-")
l=len(s)
c=l//2
first_half=s[:c]
second_half=s[c:]
if(first_half==second_half):
    print("yes")
else:
    print("No")