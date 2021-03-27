import copy
import random
from typing import Any, Dict, List, Tuple

import constructors
import drivers
import leaderboard_data
import numpy as np
import pandas as pd
from f1_objects import Constructor, Driver, Team


def compute_leaderboard_points(
    leaderboard: Dict[str, Driver],
) -> Tuple[Dict[str, float]]:

    leaderboard_names = list(leaderboard.keys())
    driver_points = {driver: 0 for driver in leaderboard_names}

    driver_points[leaderboard_names[0]] += 41  # 25 race, 3 Q3, 2 Q2, 1 Q1, 10 Q
    driver_points[leaderboard_names[1]] += 33  # 18 race, 3 Q3, 2 Q2, 1 Q1, 9 Q
    driver_points[leaderboard_names[2]] += 29  # 15 race, 3 Q3, 2 Q2, 1 Q1, 8 Q
    driver_points[leaderboard_names[3]] += 25  # 12 race, 3 Q3, 2 Q2, 1 Q1, 7 Q
    driver_points[leaderboard_names[4]] += 22  # 10 race, 3 Q3, 2 Q2, 1 Q1, 6 Q
    driver_points[leaderboard_names[5]] += 19  # 8 race, 3 Q3, 2 Q2, 1 Q1, 5 Q
    driver_points[leaderboard_names[6]] += 16  # 6 race, 3 Q3, 2 Q2, 1 Q1, 4 Q
    driver_points[leaderboard_names[7]] += 13  # 4 race, 3 Q3, 2 Q2, 1 Q1, 3 Q
    driver_points[leaderboard_names[8]] += 10  # 2 race, 3 Q3, 2 Q2, 1 Q1, 2 Q
    driver_points[leaderboard_names[9]] += 8  # 1 race, 3 Q3, 2 Q2, 1 Q1, 1 Q

    driver_points[leaderboard_names[10]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard_names[11]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard_names[12]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard_names[13]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard_names[14]] += 3  # 2 Q2, 1 Q1

    driver_points[leaderboard_names[15]] += 1  # 1 Q1
    driver_points[leaderboard_names[16]] += 1  # 1 Q1
    driver_points[leaderboard_names[17]] += 1  # 1 Q1
    driver_points[leaderboard_names[18]] += 1  # 1 Q1
    driver_points[leaderboard_names[19]] += 1  # 1 Q1

    constructor_driver_points = copy.deepcopy(driver_points)

    for rank, (driver_name, driver) in enumerate(leaderboard.items()):
        teammate = driver.teammate
        teammate_rank = leaderboard_names.index(teammate)
        if rank < teammate_rank:
            driver_points[driver_name] += 5  # 2 Q, 3 race

    return driver_points, constructor_driver_points


def compute_team_score(
    driver_points: Dict[str, float],
    constructor_driver_points: Dict[str, float],
    team: Team,
):
    score = 0

    for driver in team.drivers:
        score += driver_points[driver.name]

    for driver in team.constructor.drivers:
        score += constructor_driver_points[driver]

    score += driver_points[team.captain.name]

    return score


def monte_carlo_sample(
    N: int,
    all_drivers: List[Driver],
    all_constructors: List[Constructor],
    leaderboard: Dict[str, Driver],
) -> List[Dict[str, Any]]:

    driver_points, constructor_driver_points = compute_leaderboard_points(
        leaderboard=leaderboard
    )
    sample_teams = []

    for i in range(N):
        random_drivers = random.sample(all_drivers, 5)
        random_constructor = random.sample(all_constructors, 1)[0]

        team = Team(drivers=random_drivers, constructor=random_constructor)

        team_price = team.price
        projected_score = compute_team_score(
            driver_points, constructor_driver_points, team
        )

        sample_teams.append(
            {"team": team, "points": projected_score, "price": team_price}
        )

    return sample_teams


def sort_teams(teams: List, print_num_teams: int, output_file_name: str):
    prices = [team["price"] for team in teams]
    points = [team["points"] for team in teams]

    valid_indices = np.array(prices) < 100
    valid_points = valid_indices * np.array(points)
    highest_ranked_valid_teams = np.array(valid_points).argsort()[::-1]

    with open(output_file_name, "w") as f:
        for i in range(print_num_teams):
            f.write(f"Rank: {i}\n")
            f.write(f"   Points: {teams[highest_ranked_valid_teams[i]]['points']}\n")
            f.write(f"   Price: {teams[highest_ranked_valid_teams[i]]['price']}\n")
            f.write("   Drivers: ")
            f.write(
                repr(
                    [
                        driver.name
                        for driver in teams[highest_ranked_valid_teams[i]][
                            "team"
                        ].drivers
                    ]
                )
            )
            f.write("\n")
            f.write(
                f"   Captain: {teams[highest_ranked_valid_teams[i]]['team'].captain.name}\n"
            )
            f.write("   Constructor: ")
            f.write(repr(teams[highest_ranked_valid_teams[i]]["team"].constructor.name))
            f.write("\n")


if __name__ == "__main__":

    N = 1000000
    leaderboard = leaderboard_data.LEADERBOARD
    all_drivers = drivers.all_drivers
    all_constructors = constructors.all_constructors

    sample_teams = monte_carlo_sample(N, all_drivers, all_constructors, leaderboard)
    sort_teams(
        teams=sample_teams, print_num_teams=20, output_file_name="best_teams.txt"
    )
