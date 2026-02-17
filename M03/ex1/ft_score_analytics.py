import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    argvlen: int = len(sys.argv)
    if argvlen < 2:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return
    scores: list[str] = sys.argv[1:]
    try:
        scores = [int(x) for x in scores]
    except ValueError as e:
        print(f"Error: {e}")
    print("Score processed:", scores)
    print("Total players:", argvlen - 1)
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {(sum(scores) / argvlen):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
