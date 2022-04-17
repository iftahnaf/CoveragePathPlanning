#!/usr/bin/python3
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import CoveragePathPlanner

def main():
    scenario = Scenario()
    map = scenario.map1
    planner = CoveragePathPlanner(map)
    x, y, steps, unnecessary_steps, done = planner.offline_planning()
    if done:
        print("Map Solved, drawing...")
        scenario.draw_map(map, x, y, unnecessary_steps, sleep_dt=0.01)
        print(f"Solved in {steps} steps...")
    else:
        print("Failed to solve the map, try to increase the maximum number of repeats in offline_planning function")
        
if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)