n=int(input("Enter a number :"))
temp=n
sum=0
for i in (1,n+1):
    d=n%10
    cube=d**3
    sum=sum+cube
    n=n/10
if (sum == temp):
    print("Amstrong Number")
else:
    print("Not an amstrong number")
