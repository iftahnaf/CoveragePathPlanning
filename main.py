#!/usr/bin/python3
## This script calculates and shows the trajectory for fully coverage given 2d map.
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import CoveragePathPlanner

save_map = False
map_number = "map3" # change maps here - map1/map2/map3
show_trajectory = True

def main():
    scenario = Scenario(map_number)
    planner = CoveragePathPlanner(scenario.map)

    x, y, steps, unnecessary_steps, done = planner.swiching_gradient_planning()

    if done:
        print(f"{map_number} Solved in {steps} steps...")
        if show_trajectory:
            scenario.draw_map(scenario.map, x, y, unnecessary_steps, sleep_dt=0.005)

        if save_map:
             scenario.save_path_to_csv(x, y, map_number)
        
    else:
        print("Failed to solve the map, try to increase the maximum number of repeats in offline_planning function")
        
if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)