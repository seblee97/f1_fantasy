import argparse
import copy
import itertools
import random
from typing import Any, Dict, List, Tuple

import constructors
import drivers
import leaderboard_data
import numpy as np
import pandas as pd
import plotting_functions
import utils
from f1_objects import Constructor, Driver, Team

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--scrape_url", type=str, default=None)
arg_parser.add_argument("--budget", type=float)


def get_teams(
    all_drivers: List[Driver],
    all_constructors: List[Constructor],
    leaderboard: Dict[str, Driver],
) -> List[Dict[str, Any]]:

    all_teams = []

    driver_points, constructor_driver_points = utils.compute_leaderboard_points(
        leaderboard=leaderboard
    )

    all_driver_combinations = itertools.combinations(all_drivers, 5)

    for driver_combination in all_driver_combinations:
        eligible_captains = [
            driver for driver in driver_combination if driver.price <= 20
        ]

        for constructor in all_constructors:
            for captain in eligible_captains:
                team = Team(
                    drivers=driver_combination, constructor=constructor, captain=captain
                )
                team_price = team.price
                projected_score = utils.compute_team_score(
                    driver_points, constructor_driver_points, team
                )

                all_teams.append(
                    {"team": team, "points": projected_score, "price": team_price}
                )

    return all_teams


if __name__ == "__main__":

    args = arg_parser.parse_args()

    if args.scrape_url is not None:
        leaderboard = utils.scrape_leaderboard(args.scrape_url)
    else:
        leaderboard = leaderboard_data.LEADERBOARD

    budget = args.budget

    all_drivers = drivers.all_drivers
    all_constructors = constructors.all_constructors

    all_teams = get_teams(all_drivers, all_constructors, leaderboard)

    utils.sort_teams(
        teams=all_teams,
        print_num_teams=20,
        budget=budget,
        output_file_name="best_teams.txt",
    )

    # plotting_functions.plot_frontier(teams=sample_teams, save_path="frontier.png")
