# Problem formulation:

Given a NxM matrix, where free areas are marked with 0, obstacles with 1 and the starting point with 2, find a trajectory that passes through all the free squares with the lowest number of steps. At each step the robot can move to an adjacent (touching sides) free square. The discretisation of the grids is assumed to be equal to the width of the robot that will navigate through the space.

The answer should list the coordinates of the squares it goes through in order from the starting point, essentially the path to be taken by the robot. In addition, the code should include a simple visualisation to verify the results. I've provided you with three areas the algorithm must be able to cope with.

# General info:
The problem which I address is related to Coverege Path Planning.

# Resources

## Main papers:
1. [A survey on covarage path planning for robots](https://www.sciencedirect.com/science/article/abs/pii/S092188901300167X)
2. [Coverage Path Planning: The Boustrophedon Cellular Decomposition](https://link.springer.com/chapter/10.1007/978-1-4471-1273-0_32)
3. [Coverage path planning algorithms for agricultural field machines](https://onlinelibrary.wiley.com/doi/abs/10.1002/rob.20300)
4. [Optimal Coverage Path Planning for Arable Farming on 2D Surfaces](https://elibrary-asabe-org.ezlibrary.technion.ac.il/azdez.asp?JID=3&AID=29488&CID=t2010&v=53&i=1&T=1&refer=7&access=&dabs=Y)
5. [Spiral-STC: an on-line coverage algorithm of grid environments by a mobile robot](https://ieeexplore.ieee.org/abstract/document/1013479)

## Github
1. [Full coverage path planner ](https://github.com/nobleo/full_coverage_path_planner) - Full coverage path planning provides a move_base_flex plugin that can plan a path that will fully cover a given area.
2. [Polygon Coverage Planning](https://github.com/ethz-asl/polygon_coverage_planning)  - Coverage planning in general polygons with holes.
3. [Spiral Spanning Tree Coverage Path Planner](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/SpiralSpanningTreeCPP/spiral_spanning_tree_coverage_path_planner.py)





