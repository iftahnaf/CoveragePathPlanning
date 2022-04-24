from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, scale
import cv2

class Scenario():
    def __init__(self, map):
        if map in "map1":
            self.map = np.array([
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
        if map in "map2":
            self.map = np.array([
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
        if map in "map3":
            self.map = np.array([
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

        if map in "map4":
            self.map = np.array([
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [2, 0, 0, 0, 0, 0, 0, 0],
            ])
    def convert_to_image(self, map, output_map_image="map_1.png"): 
        # Description: convert the map to png file for testing other methods.
        # Outputs: output_map_image - png image of the matrix 
        new_map = np.where(map==2, 0, map)
        cv2.imwrite(output_map_image, 255- new_map*255)
    
    def show_path(self, map, x, y, unnecessary_steps, sleep_dt, grad_dir_along_path_shortest,dist_map=None, show_dist_map=True):
        # Description: drawing the map and the robot path in a loop.
        # Inputs: map - the given map
        #         x,y - the coordinates from the planner solution
        #         sleep_dt - dt between the map's updates.
        #         grad_dir_along_path_shortest - list of the gradient direction at each step
        #         dist_map - the calculated distance map.
        #         show_dist_map - show the distance map on the path.

        cmap = colors.ListedColormap(['White','Black', 'Blue'])

        height, _ = map.shape
        plt.figure(figsize=(8,8))

        quiver_pointer = grad_dir_along_path_shortest
        for i in range(len(quiver_pointer)):
            if quiver_pointer[i] == 0:
                quiver_pointer[i] = -1
        quiver_pointer.append(quiver_pointer[-1])

        if show_dist_map:
            for i in range(len(x)):
                plt.text(x[i]+0.25, height-y[i]-0.5, str((dist_map[y[i]][x[i]])))

        for i in range(len(x)):
            map[y[i]][x[i]] = 2
            plt.pcolor(map[::-1],cmap=cmap,edgecolors='k', linewidths=3)
            plt.scatter(x[i]+0.5, height-y[i]-0.5+0.25*quiver_pointer[i], c='Red', marker='o', linewidths=1)
            plt.quiver(x[i]+0.5, height-y[i]-0.5+0.25*quiver_pointer[i], 0, -quiver_pointer[i], color='Red')
            plt.axis('equal')
            plt.title(f"Number of steps: {i}")
            plt.pause(sleep_dt)

        cmap = colors.ListedColormap(['Black', 'Blue'])
        plt.title(f"Number of steps: {i}\n{unnecessary_steps} Steps were taken over covered squares")
        plt.pcolor(map[::-1],cmap=cmap,edgecolors='k', linewidths=3)
        plt.scatter(x[i]+0.5, height-y[i]-0.5+0.25*quiver_pointer[i], c='Red', marker='o', linewidths=2)
        plt.quiver(x[i]+0.5, height-y[i]-0.5+0.25*quiver_pointer[i], 0,-quiver_pointer[i], color='Red')
        plt.show()


    def print_path(self, map, x, y, sleep_dt):
        # Description: drawing the map - the raw version. just printing the updated map for rapid development.
        # Inputs: map - the given map
        #         x,y - the coordinates from the planner solution
        #         sleep_dt - dt between the map's updates.
        for i in range(len(x)):
            map[y[i]][x[i]] = 2
            print(map)
            plt.pause(sleep_dt)

    def save_path_to_csv(self, x, y, output_filename):
        # Description: saving the path to csv file in the results folder
        # Inputs: x,y - the coordinates from the planner solution
        #         output_filename - the name of the result file
        path = [x,y]
        np.savetxt(f"results/{output_filename}.csv", np.transpose(path), delimiter=",", fmt='%1.f', header="x,y", comments='')

