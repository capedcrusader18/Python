terms=int(input("Enter Terms "))

n1,n2=0,1
count=0

if terms<=0:
    print("Please enter positive number")
elif terms==1:
    print("Fibonacci series upto",terms,":",n1)
else:
    print("Fibonacci series :")
    while count<terms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1