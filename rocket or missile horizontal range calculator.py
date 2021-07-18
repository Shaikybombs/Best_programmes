import math


# enter the distance to be travelled.this would be helpful in finding initial velocity.
distance = int(input("Enter the distance to be travelled in km. "))

#Enter the mass of the craft.this would be helpful in calculating the force to be exerted.
mass = int(input("Enter the mass of the craft in kg. "))

#The projection angle is necessary for aligning the rocket with the distance to cover. prefered to write 45 to get the maximum range with maximum speed.
projection_angle = int(input("enter the projection angle. "))

#with above mentioned values the programme calculates the initial velocity required to cover the distance at the described projection angle.
intitial_velocity =math.sqrt(distance*10/math.sin(projection_angle)*2)

#now by finding the initial velocityt the time of flight can be calculated.
time = 2*intitial_velocity*math.sin(projection_angle)/10

#here again the initial velocity is being converted to km/hr
intitial_velocity = intitial_velocity*18/5

#once the initial velocity are calculated the acceleration can be calculated.
acceleration = intitial_velocity/time

#after knowing mass from the top and calculating the accleration the force required can be calculated.
force = mass * acceleration


#-----the results and the required values are printed by taking the important values and calculating them------
print(F"{intitial_velocity}km/hr is the initial speed")
print(f"{time}hr is the time of flight")
print(f"{force}N is the force required.")
