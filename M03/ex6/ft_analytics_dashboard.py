from typing import Generator
from random import randint
import sys


def score_generator(players: int) -> Generator[int, None, None]:
    for i in range(players):
        yield randint(500, 8000)


def ft_analytics_dashboard() -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    players: list = sys.argv[1:]
    if not players:
        players = ["alice", "bob", "charlie", "diana"]
    scgenerator: Generator[int, None, None] = score_generator(len(players))
    scores: list[int] = list(scgenerator)
    high_scores: list[str] = [
        players[i] for i in range(len(scores)) if scores[i] > 2000
    ]
    print("High scorers (>2000):", high_scores)
    double_score: list[int] = [s * 2 for s in scores]
    print("Scores doubled:", double_score)
    print(
        f"The highest scorer: {players[double_score.index(max(double_score))]}"
        f" with {max(double_score)}",
    )
    print("\n=== Dict Comprehension Examples ===")
    playersdict: dict[str, int] = {
        players[i]: scores[i] for i in range(len(players))
        }
    print("Players scores:", playersdict)
    categories: dict[str, dict[str, int]] = {
        "high": {}, "medium": {}, "low": {}}
    for item, score in playersdict.items():
        if score > 5000:
            categories["high"][item] = score
        elif score > 2000:
            categories["medium"][item] = score
        else:
            categories["low"][item] = score
    print("score categories:", categories)
    print("\n=== Set Comprehension Examples ===")
    setplayers: set[str] = set(players)
    achievements: list[str] = [
        "first_kill",
        "level_10",
        "boss_slayer",
        "explorer",
        "strategist",
        "collector",
        "speed_runner",
        "healer",
        "sharpshooter",
        "survivor",
        "builder",
        "trader",
    ]
    achievements_by_player: dict[str, set[str]] = {
        player: {
            achievements[(i + j) % len(achievements)]
            for j in range(3 + i % 3)
        }
        for i, player in enumerate(players)
    }
    active_regions: set[str] = {"north", "east", "central"}
    unique_achievements: set[str] = {
        a for s in achievements_by_player.values() for a in s}
    print("Unique players:", setplayers)
    print("Unique achievements:", unique_achievements)
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")
    total_players: int = len(setplayers)
    total_unique_achievements: int = len(unique_achievements)
    average_score: float = sum(scores) / len(scores) if scores else 0
    if scores:
        top_index: int = scores.index(max(scores))
        top_player: str = players[top_index]
        top_score: int = scores[top_index]
        top_achievements: int = len(achievements_by_player[top_player])
        print("Total players:", total_players)
        print("Total unique achievements:", total_unique_achievements)
        print(f"Average score: {average_score}")
        print(
            f"Top performer: {top_player} ({top_score} points, "
            f"{top_achievements} achievements)"
        )


if __name__ == "__main__":
    ft_analytics_dashboard()
