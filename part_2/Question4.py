
"""Calculate Euclidean distance between two points (x1,y1) and (x2,y2)"""
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Get first coordinate from user
print("Enter first coordinate:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

# Get second coordinate from user
print("\nEnter second coordinate:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Calculate and display the distance
distance = calculate_euclidean_distance(x1, y1, x2, y2)
print(f"\nThe Euclidean distance between ({x1},{y1}) and ({x2},{y2}) is {distance:.2f}")