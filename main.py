#!/usr/bin/python3
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import CoveragePathPlanner

def main():
    scenario = Scenario()
    map = scenario.map3
    planner = CoveragePathPlanner(map)
    # test = planner.calculate_distance_map()
    # print(test)
    x, y, steps, done = planner.offline_planning()
    if not done:
        print("Couldn't solve it offline, trying to solve online [IN DEVELOPMENT]")
        x, y, steps = planner.online_planning()  
    scenario.draw_map(map, x, y)
    print(f"Done in {steps} steps")

if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)
