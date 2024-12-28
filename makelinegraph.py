# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:01:30 2024

@author: Aarnav
"""
import matplotlib.pyplot as plt
#import numpy as np
import time as t

print('Welcome to Linegraph creator!')
#Just for dramatics lol
t.sleep(1)
print('Loading.....')
t.sleep(1)
print('Loading.....')
t.sleep(1)
print('Loaded!')
t.sleep(1)

def get_user_input():
    # Get the number of data points
    num_points = int(input("How many data points do you want to plot?:"))
    
    # Initialize lists to hold x and y values
    x_values = []
    y_values = []
    
    # Collect x and y values from the user
    for i in range(num_points):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

def plot_graph(x_values, y_values):
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.title('Line Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.xticks(x_values)  # Set x-ticks to the x values
    plt.yticks(y_values)  # Set y-ticks to the y values
    plt.show()

def main():
    x_values, y_values = get_user_input()
    plot_graph(x_values, y_values)

if __name__ == "__main__":
    main()
