# Display power of 2 using Anonymous Function
n=int(input("Enter a number :"))
ls=list(map(lambda x: 2**x,range(n+1)))
print(ls)
for i in range(n+1):
    print(ls[i])