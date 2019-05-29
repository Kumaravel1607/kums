kp=int(input())
sum=0
temp=kp
while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10
if kp==sum:
   print("yes")
else:
   print("no")
