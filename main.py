#!/usr/bin/python3
## This script calculates and shows the path for fully coverage given 2d map.
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import SwitchingGradientPathPlanning

save_path = False
show_path = True
map_number = "map2" # change maps here - map1/map2/map3

def main():
    scenario = Scenario(map_number)
    planner = SwitchingGradientPathPlanning(scenario.map)

    x, y, steps, unnecessary_steps, done = planner.switching_gradient_planning()

    if done:
        print(f"{map_number} Solved in {steps} steps...")
        if show_path:
            scenario.show_path(scenario.map, x, y, unnecessary_steps, sleep_dt=0.005)

        if save_path:
            scenario.save_path_to_csv(x, y, map_number)
        
    else:
        print("Failed to solve the map, try to increase the maximum number of repeats in path_planning function")
        
if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)