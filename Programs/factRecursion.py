def fact(num):
    if num==1:
        return 1
    else:
        return (num*fact(num-1))
num=7
num=int(input("Enter number to find factorial"))
result=fact(num)
print("Factorial of",num,"is",result)