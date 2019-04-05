"""wap in python to create two user defined functions add() and greatest(). the
add() function return sum of two number and greatest() function return greatest no.
in two numbers.
"""
def sum(a,b):
    return (a+b)
def greatest(a,b):
    if a>b:
        return(a)
    elif b>a:
        return(b)
a=input("Enter the number:")
b=input("Enter the number:")
print "sum of number",sum(a,b)
print "greatest of two number",greatest(a,b)

 
