import dis
from re import M
import numpy as np
import itertools

class CoveragePathPlanner():

    def __init__(self, map):
        self.map = map
        self.tmp_map = map
        self.width = self.map.shape[0]
        self.height = self.map.shape[1]
        initial_pose = np.where(self.map == 2)
        self.initial_pose = [initial_pose[0][0], initial_pose[1][0]]
        self.visited = np.zeros([self.width, self.height])
        self.done = False
        self.path = []
    
    def check_obstacle(self, pose):
        return self.map[pose[0]][pose[1]] == 1

    def check_bounderies(self, pose):
        x_bound = False
        y_bound = False
        if pose[0] > self.width-1 or pose[0] < 0 :
            x_bound = True

        if pose[1] > self.height-1 or pose[1] < 0:
            y_bound = True

        return x_bound or y_bound

    def check_passes(self, pose, route):
        counter = 0
        for i in range(len(route[0])):
            if route[1][i] == pose[1] and route[0][i] == pose[0]:
                counter = counter + 1         
        return counter

    def check_neighbors(self, pose, route, repeat_num=0, dist_map=None):
        # this is the order of the movment list directions
        right = [pose[0] + 0, pose[1] + 1]
        left = [pose[0] + 0, pose[1] - 1]
        up = [pose[0] - 1, pose[1] + 0]
        down = [pose[0] + 1, pose[1] + 0]

        neighbors = [right, left, up, down]

        movements = []
        distances = []

        for neighbor in neighbors:
            if self.check_bounderies(neighbor):
                movements.append(0)
                distances.append(0)
                continue
            if self.check_obstacle(neighbor):
                movements.append(0)
                distances.append(0)
                continue
            if self.check_passes(neighbor, route) > repeat_num:
                movements.append(0)
                distances.append(0)
                continue
            movements.append(1)
            if dist_map.all():
                distances.append(dist_map[pose[1]][pose[0]])  
        return movements, distances
    
    def calculate_distance_map(self):
        map = np.ones([self.width, self.height])
        for i in range(self.width):
            for j in range(self.height):
                if self.tmp_map[i][j] != 1:
                    distance = [self.initial_pose[0] - i, self.initial_pose[1] -j]
                    map[i][j] = np.round(np.linalg.norm(distance)) + 2
        return map

    def move_desicsion(self, movement, distances, dir="up"):
        if dir in "up":
            max_distance = 0
            for counter, move in enumerate(movement):
                if move:
                    if distances[counter] > max_distance:
                        max_distance = distances[counter]
                        indx = counter
            return indx
        else:
            min_distance = 100
            for counter, move in enumerate(movement):
                if move:
                    if distances[counter] < min_distance:
                        min_distance = distances[counter]
                        indx = counter
            return indx


    def off_line_planning(self):
        dist_map = self.calculate_distance_map()
        x = []
        y = []
        x.append(self.initial_pose[1])
        y.append(self.initial_pose[0])
        steps = 0
        repeat_num = 0
        change_dir = 0
        movement, distances = self.check_neighbors(self.initial_pose, [y, x], dist_map=dist_map)
        while not self.done:
            if not change_dir:
                indx = self.move_desicsion(movement, distances)
            else:
                indx = self.move_desicsion(movement, distances, "down")
            if indx == 0:              
                x.append(x[-1] + 1)
                y.append(y[-1] + 0)
            if indx == 1:
                x.append(x[-1] - 1)
                y.append(y[-1] - 0)
            if indx == 2:
                x.append(x[-1] + 0)
                y.append(y[-1] - 1)
            if indx == 3:
                x.append(x[-1] - 0)
                y.append(y[-1] + 1)
                
            steps = steps + 1
            movement, distances  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            if all(dir == 0 for dir in movement):
                repeat_num = repeat_num + 1
                change_dir = not change_dir
                movement, distances  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            if not np.where(self.map == 0) or repeat_num > 3:
                print(np.where(self.map == 0))
                return x, y, steps

    def on_line_planning(self):
        x = []
        y = []
        x.append(self.initial_pose[1])
        y.append(self.initial_pose[0])
        movement, _ = self.check_neighbors(self.initial_pose, [y, x])
        repeat_num = 0
        steps = 0
        while not self.done:
            
            while movement[0] and not movement[1]:
                steps = steps + 1
                x.append(x[-1] + 1)
                y.append(y[-1] + 0)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num)

            while movement[2]:
                steps = steps + 1
                x.append(x[-1] + 0)
                y.append(y[-1] - 1)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num)

            while movement[1]:
                steps = steps + 1
                x.append(x[-1] - 1)
                y.append(y[-1] - 0)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num)

            while movement[3]:
                steps = steps + 1
                x.append(x[-1] - 0)
                y.append(y[-1] + 1)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num)
                if movement[1]:
                    break

            if all(dir == 0 for dir in movement):
                repeat_num = repeat_num + 1
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num)

            if not np.where(self.map == 0) or repeat_num > 2:
                return x, y, steps