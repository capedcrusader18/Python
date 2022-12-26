num=7
factorial=1
num=int(input("Enter a Number"))
if num<0:
    print("Invalid Number")
elif num==0:
    print("The Factorial of 0 is 1")
else:
    for i  in range(1,num+1):
        factorial=factorial*i
    print("Factorial of",num,"is",factorial)