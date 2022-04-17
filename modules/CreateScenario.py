from time import sleep
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import cv2

class Scenario():
    def __init__(self):
        self.map1 = np.array([
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [ 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        self.map2 = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 2],
        ])
        self.map3 = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0],
        ])
    def convert_to_image(self, map, output_map_image="map_1.png"): 
        # Description: convert the map to png file for testing other methods.
        # Outputs: output_map_image - png image of the matrix 
        new_map = np.where(map==2, 0, map)
        cv2.imwrite(output_map_image, 255- new_map*255)
    
    def draw_map(self, map, x, y):
        cmap = colors.ListedColormap(['White','Black', 'Blue'])
        height, width = map.shape
        plt.figure(figsize=(6,6))
        for i in range(len(x)):
            map[y[i]][x[i]] = 2
            plt.pcolor(map[::-1],cmap=cmap,edgecolors='k', linewidths=3)
            plt.scatter(x[i]+0.5, height-y[i]-0.5, c='Red', marker='o')
            plt.axis('equal')
            plt.pause(0.05)
        plt.show()
        
    def print_map(self, map, x, y):
        for i in range(len(x)):
            map[y[i]][x[i]] = 2
            print(map)
            plt.pause(0.1)

        

