"""
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
"""

i=1
while i<=5:
    j=5 
    while j>i:
        print " ",
        j-=1
    num=1
    while num<=i:
        print " ",i,
        num+=1
    print
    i+=1

    
        
