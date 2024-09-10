import random

username = input("Enter Usrename: ")
if(username.find(" ") != -1):
    print("Spacing is not allowed in username!!!")
else:
    otp = random.randrange(1000,9999)
    print("OTP:",otp)
    otp2 = int(input("Enter your OTP: "))
    if(otp == otp2):
        print(f"Loading... {username}'s interface")
    else:
        print("Wrong OTP")

