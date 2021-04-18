from typing import List, Union

import matplotlib.pyplot as plt
from f1_objects import Team


def plot_frontier(teams: List[Team], save_path: Union[str, None]):
    fig = plt.figure()
    prices = [team["price"] for team in teams]
    points = [team["points"] for team in teams]
    plt.scatter(prices, points, label="random team samples")
    plt.xlabel("price")
    plt.ylabel("points")
    plt.plot(
        [100, 100],
        [0.9 * min(points), 1.1 * max(points)],
        linestyle="dashed",
        color="red",
        label="budget",
    )
    plt.legend()
    fig.show()

    if save_path is not None:
        fig.savefig(save_path, dpi=100)
