# Robot Braking Simulation 
## Overview

This project simulates the braking dynamics of a mobile robot using physics-based motion equations.  

It calculates the stopping distance based on an initial velocity and braking deceleration, and detects whether the robot would collide with an obstacle.

The simulation also visualizes the robot’s motion over time using graphs.

## Physics Model

The stopping distance is calculated using:

d = v² / (2a)

Where:
- v = initial velocity
- a = braking deceleration

Velocity over time:
v(t) = v₀ - at

Position over time:
x(t) = v₀t - ½at²

## Features

- User input for:
  - Initial velocity (m/s)
  - Braking deceleration (m/s²)
  - Obstacle distance (cm)
- Calculates stopping distance
- Simulates velocity and position over time
- Detects collisions dynamically
- Visualizes:
  - Distance vs Time curve
  - Obstacle position
  - Collision point (highlighted in red)

## Technologies Used

- Python 3
- NumPy
- Matplotlib

## How to Run

Install required libraries:

pip install numpy  
pip install matplotlib  

Then run:

python stopping_distance_project.py

## Why This Project

This project demonstrates:
- Application of physics equations in programming
- Numerical simulation using arrays
- Conditional logic for safety systems
- Data visualization
- Debugging and environment setup

It serves as a foundational robotics safety simulation.