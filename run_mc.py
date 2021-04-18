import copy
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


def monte_carlo_sample(
    N: int,
    all_drivers: List[Driver],
    all_constructors: List[Constructor],
    leaderboard: Dict[str, Driver],
) -> List[Dict[str, Any]]:

    driver_points, constructor_driver_points = utils.compute_leaderboard_points(
        leaderboard=leaderboard
    )
    sample_teams = []

    for i in range(N):
        random_drivers = random.sample(all_drivers, 5)
        random_constructor = random.sample(all_constructors, 1)[0]

        team = Team(drivers=random_drivers, constructor=random_constructor)

        team_price = team.price
        projected_score = utils.compute_team_score(
            driver_points, constructor_driver_points, team
        )

        sample_teams.append(
            {"team": team, "points": projected_score, "price": team_price}
        )

    return sample_teams


if __name__ == "__main__":

    N = 5000000
    leaderboard = leaderboard_data.LEADERBOARD
    all_drivers = drivers.all_drivers
    all_constructors = constructors.all_constructors

    sample_teams = monte_carlo_sample(N, all_drivers, all_constructors, leaderboard)
    utils.sort_teams(
        teams=sample_teams, print_num_teams=20, output_file_name="best_teams.txt"
    )

    # plotting_functions.plot_frontier(teams=sample_teams, save_path="frontier.png")
