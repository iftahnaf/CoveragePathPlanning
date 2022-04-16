import numpy as np
import itertools

class CoveragePathPlanner():

    def __init__(self, map):
        self.map = map
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

    def check_neighbors(self, pose, route):
        # this is the order of the movment list directions
        right = [pose[0] + 0, pose[1] + 1]
        left = [pose[0] + 0, pose[1] - 1]
        up = [pose[0] - 1, pose[1] + 0]
        down = [pose[0] + 1, pose[1] + 0]

        neighbors = [right, left, up, down]

        movements = []

        for neighbor in neighbors:
            if self.check_bounderies(neighbor):
                movements.append(0)
                continue
            if self.check_obstacle(neighbor):
                movements.append(0)
                continue
            if self.check_passes(neighbor, route) > 0:
                movements.append(0)
                continue
            movements.append(1)   
        return movements

    def plan(self):
        x = []
        y = []
        x.append(self.initial_pose[1])
        y.append(self.initial_pose[0])
        movement = self.check_neighbors(self.initial_pose, [y, x])
        while not self.done:
            
            while movement[0]:
                x.append(x[-1] + 1)
                y.append(y[-1] + 0)
                movement = self.check_neighbors([y[-1], x[-1]], [y, x])
            while movement[2]:
                x.append(x[-1] + 0)
                y.append(y[-1] - 1)
                movement = self.check_neighbors([y[-1], x[-1]], [y, x])
            while movement[1]:
                x.append(x[-1] - 1)
                y.append(y[-1] - 0)
                movement = self.check_neighbors([y[-1], x[-1]], [y, x])
            while movement[3]:
                x.append(x[-1] - 0)
                y.append(y[-1] + 1)
                movement = self.check_neighbors([y[-1], x[-1]], [y, x])
            if all(dir == 0 for dir in movement):
                print("Done solve")
                return x, y