# -*- coding: utf-8 -*-
"""

lambda exercise
Create the carpet program 
    get the length , width and distance from the enduser
    then create all calculations  with all lambda functions
    calcArea
    calcCarpetPrice
    calcTravel : distance < 10 then tf = 0
    > 10 and < 20 then tf = 10
    else tf = 20

"""

calcArea        = lambda l, w : l * w
calcCarpetprice = lambda area : area * 10
calcTravelFee   = lambda d : 0 if d < 0 else ( 20 if d > 20 else 10)
calcTotal       = lambda cp, tf : cp + tf

length      = float ( input ("Please enter length" ) )
width       = float ( input ("Please enter width" ) )
distance    = float ( input ("Please enter distance" ) )

area        = calcArea(length, width)  # use result with input parameters 2 and 3 , show the input and the output
cp          = calcCarpetprice(area)
travelfee   = calcTravelFee(distance)
total       = calcTotal(cp,travelfee)

print ( "area:".ljust(15), area )
print ( "carpet price:".ljust(15), cp )
print ( "travel fee:".ljust(15), travelfee )
print ( "total:".ljust(15), total)











result = lambda x, y : 5 if x > y else ( 18 if x == 2 else 0)
print (result(1,3))  # use result with input parameters 2 and 3 , show the input and the output

result = lambda x, y : 5 if x > y else ( 18 if x == 2 else 0)
print (result(5,3))  # use result with input parameters 2 and 3 , show the input and the output


result = lambda x, y : 5 if x > y else ( 18 if x == 2 else 0)
print (result(2,3))  # use result with input parameters 2 and 3 , show the input and the output




