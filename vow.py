k=input()
list=["a","e","i","o","u","A","E","I","O","U"]
if k.isalpha():
    if k in list:
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")
