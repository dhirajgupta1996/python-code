sal=input("enter the salary:")
if sal>1 and sal<4000:
    hra=(10*sal)/100
    da=(50*sal)/100
    g.a=sal+hra+da
    print"gross salary=",g.a
elif sal>4000 and sal<8000:
    hra=(20*sal)/100
    da=(60*sal)/100
    sal=sal+hra+da
    print "gross salary=",sal
elif sal>8000 and sal<12000:
    hra=(25*sal)/100
    da=(70*sal)/100
    sal=sal+hra+da
    print "gross salary=",sal
elif sal>12000:
    hra=(30*sal)/100
    da=(80*sal)/100
    sal=sal+hra+da
    print "gross salary=",sal
            
