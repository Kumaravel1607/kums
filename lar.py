l=list(map(int,input().split()))
am=l[0]
bm=l[1]
cm=l[2]
if am>=bm and am>=cm:
    print(am)
elif bm>=am and bk>=cm:
    print(bm)
else:
    print(cm)
