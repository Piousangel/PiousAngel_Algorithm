while True:
    val = str(input())
    if int(val) == 0:
        break
    str1 = ""
    str2 = ""
    if(len(val)%2 == 0):
        str1 = val[0:len(val)//2]
        str2 = val[len(val)//2: ]
    else:
        str1 = val[0:(len(val)-1)//2]
        str2 = val[(len(val)-1)//2+1: ]
               

    if str1 == str2[::-1] :
        print("yes")
    else:
        print("no")