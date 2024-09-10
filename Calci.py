import math

operation = input("Enter operation {+ - / * ^ }: ")

if(operation == "^"):
     num1 = float(input("Enter base number: "))
     print(f"Enter power ({int(num1)}^ ?): ")
     num2 = int(input())
     print("Answer: ",pow(num1, num2))
else:
     num1 = float(input("Enter 1st number: "))
     num2 = float(input("Enter 2nd number: "))
     if(operation == "+"):
           print("Answer: ",num1+num2)
     elif(operation == "-"):
           print("Answer: ",num1-num2)
     elif(operation == "/"):
           print("Answer: ",num1/num2)
     elif(operation == "*"):
           print("Answer: ",num1*num2)
     else:
          print(operation," is a invalid operation")
  