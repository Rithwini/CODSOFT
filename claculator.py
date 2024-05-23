def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2==0:
        return "error! division by zero"
    else:
        return num1/num2

def modulus(num1,num2):
    return num1%num2

print("Select Operation :")
print("1.Addition")
print("2.Subtraction")
print("3.Multipication")
print("4.Division")
print("5.Modulus")

while True:

    choice = (input("Enter choice (1/2/3/4/5):"))

    if choice in ('1','2','3','4','5'):
        num1=float(input("Enter First Number:"))
        num2=float(input("Enter Second Number:"))

        if choice == '1':
            print("Result = ",addition(num1,num2))
        elif choice == '2':
            print("Result = ",subtraction(num1,num2))
        elif choice == '3':
             print("Result = ",multiplication(num1,num2))
        elif choice == '4':
             print("Result = ",division(num1,num2))
        elif choice == '5':
             print("Result = ",modulus(num1,num2))
        break
    else:
        print("Invalid Input")
