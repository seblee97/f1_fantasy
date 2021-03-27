import pandas as pd
from f1_objects import Constructor, Driver, Team


def compute_points(
    team: Team, leaderboard: List[str], driver_data: pd.DataFrame
) -> float:

    driver_points = {driver: 0 for driver in leaderboard}
    constructor_driver_points = {driver: 0 for driver in leaderboard}

    driver_points[leaderboard[0]] += 41  # 25 race, 3 Q3, 2 Q2, 1 Q1, 10 Q
    driver_points[leaderboard[1]] += 33  # 18 race, 3 Q3, 2 Q2, 1 Q1, 9 Q
    driver_points[leaderboard[2]] += 29  # 15 race, 3 Q3, 2 Q2, 1 Q1, 8 Q
    driver_points[leaderboard[3]] += 25  # 12 race, 3 Q3, 2 Q2, 1 Q1, 7 Q
    driver_points[leaderboard[4]] += 22  # 10 race, 3 Q3, 2 Q2, 1 Q1, 6 Q
    driver_points[leaderboard[5]] += 19  # 8 race, 3 Q3, 2 Q2, 1 Q1, 5 Q
    driver_points[leaderboard[6]] += 16  # 6 race, 3 Q3, 2 Q2, 1 Q1, 4 Q
    driver_points[leaderboard[7]] += 13  # 4 race, 3 Q3, 2 Q2, 1 Q1, 3 Q
    driver_points[leaderboard[8]] += 10  # 2 race, 3 Q3, 2 Q2, 1 Q1, 2 Q
    driver_points[leaderboard[9]] += 8  # 1 race, 3 Q3, 2 Q2, 1 Q1, 1 Q

    driver_points[leaderboard[10]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard[11]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard[12]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard[13]] += 3  # 2 Q2, 1 Q1
    driver_points[leaderboard[14]] += 3  # 2 Q2, 1 Q1

    driver_points[leaderboard[15]] += 1  # 1 Q1
    driver_points[leaderboard[16]] += 1  # 1 Q1
    driver_points[leaderboard[17]] += 1  # 1 Q1
    driver_points[leaderboard[18]] += 1  # 1 Q1
    driver_points[leaderboard[19]] += 1  # 1 Q1
    driver_points[leaderboard[20]] += 1  # 1 Q1

    constructor_driver_points = copy.deepcopy(driver_points)

    for rank, driver in enumerate(leaderboard):
        teammate = np.array(driver_data[driver_data.Names == driver].Teammates)[0]
        teammate_rank = leaderboard.index(teammate)
        if rank < teammate_rank:
            driver_points[driver] += 5  # 2 Q, 3 race

    score = 0

    for driver in team.drivers:
        score += driver_points[driver.name]

    for driver in team.constructor.drivers:
        score += constructor_driver_points[driver]

    score += driver_points[team.captain.name]

    return score


def monte_carlo_sample(N: int) -> List[Dict[str, Any]]:
    sample_teams = []

    for i in range(N):
        random_drivers = random.sample(all_drivers, 5)
        random_constructor = random.sample(all_constructors, 1)[0]

        team = Team(drivers=random_drivers, constructor=random_constructor)

        team_price = team.price
        projected_score = compute_points(team, leaderboard, drivers)

        sample_teams.append(
            {"team": team, "points": projected_score, "price": team_price}
        )

    return sample_teams
