import copy
from typing import Any, Dict, List, Tuple

import constants
import drivers
import numpy as np
import requests
from bs4 import BeautifulSoup
from f1_objects import Constructor, Driver, Team

NAME_DRIVER_MAPPING = {
    constants.LEWIS_HAMILTON: (constants.HAMILTON, drivers.hamilton),
    constants.MAX_VERSTAPPEN: (constants.VERSTAPPEN, drivers.verstappen),
    constants.VALTTERI_BOTTAS: (constants.BOTTAS, drivers.bottas),
    constants.SERGIO_PEREZ: (constants.PEREZ, drivers.perez),
    constants.CHARLES_LECLERC: (constants.LECLERC, drivers.leclerc),
    constants.PIERRE_GASLY: (constants.GASLY, drivers.gasly),
    constants.DANIEL_RICCIARDO: (constants.RICCIARDO, drivers.ricciardo),
    constants.LANDO_NORRIS: (constants.NORRIS, drivers.norris),
    constants.CARLOS_SAINZ: (constants.SAINZ, drivers.sainz),
    constants.YUKI_TSUNODA: (constants.TSUNODA, drivers.tsunoda),
    constants.LANCE_STROLL: (constants.STROLL, drivers.stroll),
    constants.FERNANDO_ALONSO: (constants.ALONSO, drivers.alonso),
    constants.SEBASTIAN_VETTEL: (constants.VETTEL, drivers.vettel),
    constants.ESTEBAN_OCON: (constants.OCON, drivers.ocon),
    constants.GEORGE_RUSSELL: (constants.RUSSELL, drivers.russell),
    constants.NICHOLAS_LATIFI: (constants.LATIFI, drivers.latifi),
    constants.KIMI_RAIKKONEN: (constants.RAIKKONEN, drivers.raikkonen),
    constants.ANTONIO_GIOVINAZZI: (constants.GIOVINAZZI, drivers.giovinazzi),
    constants.NIKITA_MAZEPIN: (constants.MAZEPIN, drivers.mazepin),
    constants.MICK_SCHUMACHER: (constants.SCHUMACHER, drivers.schumacher),
}


def scrape_leaderboard(url: str):
    driver_order_names = oddschecker_order(url)
    drivers = {
        NAME_DRIVER_MAPPING[driver][0]: NAME_DRIVER_MAPPING[driver][1]
        for driver in driver_order_names
    }
    return drivers


def oddschecker_order(oddschecker_url: str):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"
    headers = {"User-Agent": user_agent}
    oddschecker_page = requests.get(oddschecker_url, headers=headers)
    soup = BeautifulSoup(oddschecker_page.content, "html.parser")
    drivers = soup.find(id="t1").find_all(class_="diff-row evTabRow bc")
    driver_names = [driver.find("a")["data-name"] for driver in drivers]
    return driver_names


def sort_teams(
    teams: List, print_num_teams: int, output_file_name: str, budget: float = 100
):
    prices = [team["price"] for team in teams]
    points = [team["points"] for team in teams]

    valid_indices = np.array(prices) < budget
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

    print(driver_points)
    print(constructor_driver_points)

    return driver_points, constructor_driver_points
