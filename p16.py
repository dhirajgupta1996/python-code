#wap to calculate volume and surface area of cuboid using function
def volume(x,y,z):
    return (x*y*z)
def surfacearea(x,y,z):
    return (2*(x*y+y*z+z*x))
l=input("Enter length:")
b=input("Enter breadth:")
h=input("Enter height:")
print "volume of cuboid",volume(l,b,h)
print "surface area of cuboid",surfacearea(l,b,h)
