import dis
from re import M
from time import sleep
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
        # Description: checks if pose is on obstacle
        # Inputs: pose - the next robot position.
        # Outputs: return 1 if pose is an obstacle.
        return self.map[pose[0]][pose[1]] == 1

    def check_bounderies(self, pose):
        # Description: if pose is in the given map. return True if it is outside of the map.
        # Inputs: pose - the next robot position.
        # Outputs: return 1 if pose is out of bounds.
        x_bound = False
        y_bound = False
        if pose[0] > self.width-1 or pose[0] < 0 :
            x_bound = True

        if pose[1] > self.height-1 or pose[1] < 0:
            y_bound = True

        return x_bound or y_bound

    def check_passes(self, pose, route):
        # Description: count how many times the robot visited in pose.
        # Inputs: pose - the next robot position.
        #         route - the x,y coordinate list of the robots passed positions.
        # Outputs: counter - how many times the robot visited in the pose.
        counter = 0
        for i in range(len(route[0])):
            if route[1][i] == pose[1] and route[0][i] == pose[0]:
                counter = counter + 1    
        return counter

    def check_neighbors(self, pose, route, repeat_num=1, dist_map=None):
        # Description: check allowed movments and distances of the next step
        # Inputs: pose - the current robot position.
        #         route - the x,y coordinate list of the robots passed positions.
        #         repeat_num(1 default) - the number of allowed visits per coordinate
        #         dist_map(None default) - the distances map
        # Outputs: movments - 1d array, order: right, left, up down. 1 is allowed movment.
        #          distances - 1d array, same order as movement, represents the distance number of each position.
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
                distances.append(dist_map[neighbor[0], neighbor[1]])  
        return movements, distances
    
    def calculate_distance_map(self):
        # Description: create a distance 2d map, round the norm of the distance.
        # Outputs: map - 2d array, each element is some distance from the starting point.
        map = np.ones([self.width, self.height])
        for i in range(self.width):
            for j in range(self.height):
                if self.tmp_map[i][j] != 1:
                    distance = [self.initial_pose[0] - i, self.initial_pose[1] -j]
                    map[i][j] = np.round(np.linalg.norm(distance)) + 2
        return map

    def iftach_switching_gradient(self, movement, distances, pose, dir="up"):
        # Description: decide what the next move should be, I call it iftach switching gradient method.
        # we move along the gradient of the distances map, when we reach the end of the map start move along the negative gradient of the distances map.
        # also, if two direction has the same values, we check which has most visited and take the other one(in the offline_planning function). inspired by the wavefront CPP method.
        # Inputs: movement - 1d array with the allowed direction of movment.
        #         distances - 1d array with the distances of each movement. 0 for prohibited movement.
        #         pose - the current position of the robot.
        # Outputs: indx - the index number of the choosen movement.
        indx = 0
        if dir in "up":
            max_distance = 0
            for counter, move in enumerate(movement):
                if move:
                    if distances[counter] >= max_distance:
                        max_distance = distances[counter]
                        indx = counter
            return indx
        else:
            min_distance = 10000
            for counter, move in enumerate(movement):
                if move:
                    if distances[counter] <= min_distance:
                        min_distance = distances[counter]
                        indx = counter
            return indx  

    def offline_planning(self):
        # Description: iteratively calls iftach switching gradient and updates the route accordingly. allowed repeated
        # visiting is reseting every time there is a new movement allowed.
        # Outputs: x,y - list of the coordinates during the lawn mowing.
        #           steps - the number of steps to fully cover the map.
        #           unnecessary_steps - the number of steps the robot did on an visiten coordinate.
        #           1/0 - 1 if the robot successfully covered the map.
        self.visit_map = np.zeros([self.width, self.height])
        self.visit_map = np.where(self.map == 1, 1, 0)
        self.visit_map[self.initial_pose[0]][self.initial_pose[1]] = 1
        unnecessary_steps  = 0
        dist_map = self.calculate_distance_map()
        x = []
        y = []
        x.append(self.initial_pose[1])
        y.append(self.initial_pose[0])

        steps = 0
        change_dir = 0

        movement, distances = self.check_neighbors(self.initial_pose, [y, x], dist_map=dist_map)

        while not self.done:
            repeat_num = 0

            if not change_dir:
                indx = self.iftach_switching_gradient(movement, distances, [y[-1], x[-1]])
            else:
                indx = self.iftach_switching_gradient(movement, distances, [y[-1], x[-1]], "down")

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

            self.visit_map[y[-1]][x[-1]] = self.visit_map[y[-1]][x[-1]] +1 
            if self.visit_map[y[-1]][x[-1]] > 1:
                unnecessary_steps = unnecessary_steps +1
            steps = steps + 1
            movement, distances  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            if ( self.visit_map != 0 ).all():
                self.done = True

            while all(dir == 0 for dir in movement):
                repeat_num = repeat_num + 1
                change_dir = not change_dir # when stuck, choose direction randomly
                movement, distances  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            if repeat_num > 10:
                return x, y, steps, 0

        return x, y, steps, unnecessary_steps, 1

    def online_planning(self):


        # ********** EXPERIMENTAL FOR DEVELOPERS ONLY ;) **********


        # Description: an online option when the map is not given.
        # Outputs: x,y - list of the coordinates during the lawn mowing.
        #           steps - the number of steps to fully cover the map.
        dist_map = np.zeros([self.width, self.height])
        x = []
        y = []
        x.append(self.initial_pose[1])
        y.append(self.initial_pose[0])
        movement, _ = self.check_neighbors(self.initial_pose, [y, x], dist_map=dist_map)
        repeat_num = 0
        steps = 0
        while not self.done:
            
            while movement[0] and not movement[1]:
                steps = steps + 1
                x.append(x[-1] + 1)
                y.append(y[-1] + 0)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            while movement[2]:
                steps = steps + 1
                x.append(x[-1] + 0)
                y.append(y[-1] - 1)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            while movement[1]:
                steps = steps + 1
                x.append(x[-1] - 1)
                y.append(y[-1] - 0)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            while movement[3]:
                steps = steps + 1
                x.append(x[-1] - 0)
                y.append(y[-1] + 1)
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)
                if movement[1]:
                    break

            if all(dir == 0 for dir in movement):
                repeat_num = repeat_num + 1
                movement, _  = self.check_neighbors([y[-1], x[-1]], [y, x], repeat_num, dist_map=dist_map)

            if not np.where(self.map == 0) or repeat_num > 2:
                return x, y, steps