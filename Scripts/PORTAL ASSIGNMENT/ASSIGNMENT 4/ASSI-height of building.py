# calculate the height of a building in feet, 
# given distance of the observer from the building in meters and 
# the angle formed at the observation point given in degrees.

import math
distance = float(input("Enter the distance between the building and the observer in meters: "))
angle = float(input("Enter the angle formed at the observation point in degrees: "))  #angle in degree 
angle_radians = angle * (3.14159 / 180)   #angle in radian
height = distance * (math.tan(angle_radians))  #height in meters by tan = perpendicular/base
height_feet = height * 3.281    #height from meter to feet 
print("Height of the building in feet:", height_feet)