#Stopping distance calculator
#This script calculates stopping distance using basic motion equations.
print("Stopping Distance Simulation")
print("----------------------------")
def calculate_stopping_distance (initial_speed, deceleration):
    return (initial_speed ** 2) / (2 * deceleration)
# the function takes 2 inputs (initial_speed(v)) and deceleration(a)), and uses them for the formula d= v^2/(2a) to return stopping distance.
#the **2 means initial_speed squared. We square it because the equation for stopping distance is d= v^2/(2a), which comes from v^2 = u^2 + 2as

#Ask for user input
initial_speed = float(input("Enter initial speed (m/s): "))
deceleration = float (input("Enter deceleration (m/s^2): ")) 

import numpy as np
import matplotlib.pyplot as plt

#Time until stop
t_stop = initial_speed / deceleration

#Time array
t = np.linspace(0, t_stop, 500)

#Velocity over time
v = initial_speed - deceleration * t

#Distance over time
x = initial_speed * t - 0.5 * deceleration * t**2

#Distance to cm
x_cm = x * 100

#Prevent division by zero
if deceleration == 0:
    print ("Deceleration cannot be zero. It must be grater than 0.")
else:
    distance = calculate_stopping_distance (initial_speed, deceleration)
    distance_cm = distance * 100
    print (f"Stopping distance: {distance_cm:.2f} cm") 
#We prevent dividing by 0 because division by 0 is undefined. If deceleration is 0, it means the robot never slows down --> never stops
# ".2f" means "display the distance with 2 decimal places"
#stopping distance increases with the square of speed, meaning that if speed doubles, stopping distance becomes 4 times larger.

obstacle_distance_cm = float(input("Enter obstacle distance(cm)"))
collision = False

for i in range(len(t)):
    if x_cm[i] >= obstacle_distance_cm:
        print ("COLLISION DETECTED at time:", round(t[i], 2), "seconds")
        collision = True
        collision_index = i
        break
if not collision:
    print ("Robot stopped safely before the obstacle")
    

#Plot velocity
plt.figure()
plt.plot(t, v, color= 'green')
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.show()

#Plot distance
plt.figure() #creates the canvas (plt.plot draws on it)
if collision:
    plt.plot(t[:collision_index],
             x_cm[:collision_index],
             color='green',
             linestyle='-') #before collision
    plt.plot(t[collision_index:], 
             x_cm[collision_index:],
             color='red',
             linestyle='--') #the trahectory it would have followed if it hadn't crashed
    plt.scatter(t[collision_index], 
             x_cm[collision_index],
             color='red', s=100) #collision point
else:
    plt.plot(t, x_cm, color='green')
plt.axhline(y=obstacle_distance_cm, linestyle='--') #obstacle line
plt.title("Distance vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Distance (cm)")
plt.show()