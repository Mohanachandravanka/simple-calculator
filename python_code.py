print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Division")
option =int(input("choose an operation:"))
result = 05
if(option in [1,2,3,4]):
    num1=int(input("Enter first numnber:"))
    num2=int(input("Enter second numnber:"))

    if(option == 1):
        result=num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result=num1 * num2
    elif(option == 4):
        result=num1 // num2
else:
    print("Invalid operation entered")

print("The result of the operation is {}".format(result))