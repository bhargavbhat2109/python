pwd=input("Enter your password: ")
a=len(pwd)
if a==8:
    print("Your password is valid")
elif a<8:
    print("Your password is too short")
else:
    print ("your password is very strong")