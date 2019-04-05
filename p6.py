#Temperature converter

print "Enter 1 for c to f"
print "Enter 2 for f to c"
ch= input()
if ch==1:
    c=input("Enter temperature in c:")
    f=(9*c)/5+32
    print "Temperature in f=",f
elif ch==2:
    f=input("Enter temperature in f:")
    c=(f-32)*5/9
    print "Temperature in c=",c
else:
    print "Invalid choice"
