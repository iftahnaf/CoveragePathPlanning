#!/usr/bin/python3
## This script calculates and shows the path for fully coverage given 2d map.
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import SwitchingGradientPathPlanning

save_path = False
map_number = "map3" # change maps here - map1/map2/map3
show_path = True

def main():
    scenario = Scenario(map_number)
    planner = SwitchingGradientPathPlanning(scenario.map)

    x, y, steps, unnecessary_steps, done = planner.swiching_gradient_planning()

    if done:
        print(f"{map_number} Solved in {steps} steps...")
        if show_path:
            scenario.draw_map(scenario.map, x, y, unnecessary_steps, sleep_dt=0.1)

        if save_path:
             scenario.save_path_to_csv(x, y, map_number)
        
    else:
        print("Failed to solve the map, try to increase the maximum number of repeats in offline_planning function")
        
if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)