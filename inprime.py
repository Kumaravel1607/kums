kp,kk=map(int,input().split())
for i in range(kp,kk+1):
    if(i>1):
        for k in range(2,i):
            if(i%k)==0:
                break
        else:
            print(i,end=' ')
print()
