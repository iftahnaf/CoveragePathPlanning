# Problem formulation:

Given a NxM matrix, where free areas are marked with 0, obstacles with 1 and the starting point with 2, find a trajectory that passes through all the free squares with the lowest number of steps. At each step the robot can move to an adjacent (touching sides) free square. The discretisation of the grids is assumed to be equal to the width of the robot that will navigate through the space.

# General info:

This repository contains Coverage Path Planning algorithm calls Swiching Gradient CPP.
The Swiching Gradient CPP is an offline algorithm which minimize the number of needed steps to fully cover the free squares of an entire 2D map with obstacles.

# Swiching Gradient method:

The algorithm works as follow:

* Create a new 2D map, with the same dimensions as the original map. each element in the new map is the value of the distance between the starting point and the element (different distances method can be considered).

* At each step, check which direction is O.K to move with 2 restrictions: the neighbor square should not be an obstacle and it should be in bounds. 

* The algorithm prefers newly neighbors rather than visited ones.

* The next series of steps will be in the positive or negative direction of the distances map. 
At each time we reached the end of the gradient (meaning the local maximum or minimum of the distances map) we switch to the oppisite direction of the gradient.

* When all suqares are visited, return the path.

* Becuase the sensativity to the starting direction of the gradient and the swiching policy, for each map we check those 2 hyper-parameters combinations and takes the one that minimize the steps number.


of Zelinsky, 1993, `Planning Paths of Complete Coverage of an Unstructured Environment by a Mobile Robot`.

# Install:

        git clone https://github.com/iftahnaf/CoveragePathPlanning.git

# Run:

        cd ~/CoveragePathPlanning
        python main.py

## Settings:

1. `save_path` - if True, the robot's path will be saved as a `.csv` file in the `result` folder.

2. `map_number` - The map number from `CreateScenario` class in the `modules` folder. You can add new maps with the same formation.

3. `show_path` - Plotting the shortest path given by Swiching Gradient CPP algorithem.

# Resources

## Main papers:
1. [A survey on covarage path planning for robots](https://www.sciencedirect.com/science/article/abs/pii/S092188901300167X)
2. [Coverage Path Planning: The Boustrophedon Cellular Decomposition](https://link.springer.com/chapter/10.1007/978-1-4471-1273-0_32)
3. [Planning Paths of Complete Coverage of an Unstructured Environment by a Mobile Robot](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.53.7617&rep=rep1&type=pdf)
4. [Spiral-STC: an on-line coverage algorithm of grid environments by a mobile robot](https://ieeexplore.ieee.org/abstract/document/1013479)

## Github
1. [Full coverage path planner ](https://github.com/nobleo/full_coverage_path_planner) - Full coverage path planning provides a move_base_flex plugin that can plan a path that will fully cover a given area.
2. [Polygon Coverage Planning](https://github.com/ethz-asl/polygon_coverage_planning)  - Coverage planning in general polygons with holes.
3. [Spiral Spanning Tree Coverage Path Planner](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/SpiralSpanningTreeCPP/spiral_spanning_tree_coverage_path_planner.py)





