l=900
u=1000

print("Prime Numbers between",l,"and",u)

for num in range(l,u+1):
    if num>1:
        for i in range(2, num):
            if (num%i)==0:
                break
        else:
            print(num)
