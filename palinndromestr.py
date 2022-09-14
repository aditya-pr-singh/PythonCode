from re import S


s=input("Enter a string:-")
if(s==s[::-1]):
    print("string is palindrome")
else:
    print("not palindrome")
