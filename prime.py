kp = int(input())
if kp> 1:
    for i in range(2,kp):
        if (kp% i) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("yes")
