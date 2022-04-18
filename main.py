#!/usr/bin/python3
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import CoveragePathPlanner

save_map = False
map_number = "map3" # change maps here - map1/map2/map3

def main():
    scenario = Scenario(map_number)
    map = scenario.map 
    planner = CoveragePathPlanner(map)
    x, y, steps, unnecessary_steps, done = planner.offline_planning()
    if done:
        if save_map:
             scenario.save_path_to_csv(x, y, map_number)
        print(f"{map_number} Solved, drawing...")
        scenario.draw_map(map, x, y, unnecessary_steps, sleep_dt=0.005)
        print(f"Solved in {steps} steps...")
    else:
        print("Failed to solve the map, try to increase the maximum number of repeats in offline_planning function")
        
if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)