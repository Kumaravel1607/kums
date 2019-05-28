k=int(input())
if(k%4==0 and k%100!=0 or k%400==0):
    print("Yes")
else:
    print("No")
