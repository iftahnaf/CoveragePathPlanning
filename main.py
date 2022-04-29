#!/usr/bin/python3
## This script calculates and shows the path for fully coverage given 2d map.
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import SwitchingGradientPathPlanning

save_path = False
show_path = True
map_number = "map4" # change maps here - map1/map2/map3

def main():
    scenario = Scenario(map_number)
    planner = SwitchingGradientPathPlanning(scenario.map)
    dist_map = planner.calculate_distance_map(planner.initial_pose)
    x, y, steps, unnecessary_steps, grad_dir_along_path_shortest, hyper_paramaters, done = planner.switching_gradient_planning()

    if done:
        print(f"\n{map_number} Solved in {steps} steps, {unnecessary_steps} steps were unnecessary...\n\nHyper-Parameters:\n\n    Starting Direction: {hyper_paramaters.pop()}\n    Distance Calculation: {hyper_paramaters.pop()}\n    Gradient's changing policy: {hyper_paramaters.pop()}\n\n")
        if show_path:
            scenario.show_path(scenario.map, x, y, unnecessary_steps, sleep_dt=0.005, grad_dir_along_path_shortest=grad_dir_along_path_shortest, dist_map=dist_map, show_dist_map=True)

        if save_path:
            scenario.save_path_to_csv(x, y, map_number)
        
    else:
        print("Failed to solve the map, try to increase the maximum number of repeats in path_planning function")
        
if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)
