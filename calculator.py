

print("select operation")
print("1 addition")
print("2 subtraction")
print("3 multiplication")
print("4 divide")

choice = input("enter your choice (1,2,3,4):  \n")

num1 = float(input("enter your number 1: "))
num2 = float(input("enter your number 2: "))

if choice == '1':
    print(num1+num2)

elif choice == '2':
    print(num1-num2)

elif choice == '3':
    print(num1*num2)

elif choice == '4':
    print(num1/num2)

else:
    print("invalid output")


