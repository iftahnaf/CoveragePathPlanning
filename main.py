#!/usr/bin/python3
from modules.CreateScenario import Scenario
from modules.CoveragePathPlanner import CoveragePathPlanner

def main():
    scenario = Scenario()
    map = scenario.map1
    planner = CoveragePathPlanner(map)
    distance_map = planner.calculate_distance_map()
    print(distance_map)
    x, y, steps = planner.plan()
    # scenario.draw_map(map, x, y)
    print(f"Done in {steps} steps")

if __name__ =="__main__":
    try:
        main()
    except Exception as e:
        print(e)
