# Problem formulation:

Given a NxM matrix, where free areas are marked with 0, obstacles with 1 and the starting point with 2, find a trajectory that passes through all the free squares with the lowest number of steps. At each step the robot can move to an adjacent (touching sides) free square. The discretisation of the grids is assumed to be equal to the width of the robot that will navigate through the space.

The answer should list the coordinates of the squares it goes through in order from the starting point, essentially the path to be taken by the robot. In addition, the code should include a simple visualisation to verify the results. I've provided you with three areas the algorithm must be able to cope with.

# General info:
Coverage Path Planning algorithm for given map, meaning offline solution. My solution based on the paper
by Zelinsky, 1993, `Planning paths of complete coverage of an unstructured environment by a mobile robot`.

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





