#Electricity Bill Calcultion
"""
1-150                   2.40/unit
for next 151-300        3.00/unit
for next more than 300  3.20/unit
"""
con_name=raw_input("Enter consumer name:")
unit=input("Enter number of unit comsume:")
if unit<=150:
    bill=unit*2.40
elif unit>150 and unit<=300:
    bill=(150*2.40)+(unit-150)*3.00
else:
    bill=(150*2.40)+(150*3.00)+(unit-300)*3.20
print "Hello!",con_name,"Your bill is",bill,"rupees"    
