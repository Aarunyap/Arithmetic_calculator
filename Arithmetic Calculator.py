flag = "Yes"
print("SCIENTIFIC CALCULATOR \n\n")
def factorial(m):
    fact = 1
    for n in range(1,m+1):
        fact = fact*n
    print(fact)
    
    
while flag == "Yes":
    num1 = float(input("Enter number 1 "))
    opr = input("Enter an operation ")
    if opr!="!":
       num2 = float(input("Enter number 2 "))
    result = 0
    if opr=="+":
       result = num1 + num2
       print(result)
    elif opr=="-":
       result = num1 - num2
       print(result)
    elif opr=="*":
       result = num1*num2
       print(result)
    elif opr=="/":
       result = num1/num2
       print(result)
    elif opr=="%":
        result = num1%num2
        print(result)
    elif opr=="**" or opr=="^":
        result = int(num1)**int(num2)
        print(result)
    elif opr=="!":
        factorial(int(num1))
    else:
       print("Invalid arithmetic operator ")

    print("\n\nDo you wish to continue? ")
    flag=input()
    

    
    
