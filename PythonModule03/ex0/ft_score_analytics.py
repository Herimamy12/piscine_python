#!/usr/bin/env python3


import sys


def ft_score_analytics():
    scores = []
    if len(sys.argv) < 2:
        print("Usage: python3 ft_command_quest.py <score1> <score2> ...")
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Warning: Invalid score '{arg}'. Ignored.")
    if not scores:
        return {"count": 0, "average": 0, "max": None, "min": None}

    print("Operations analytics:")
    print(f"len(scores) = {len(scores)}")
    print(f"sum(scores) = {sum(scores)}")
    print(f"max(scores) = {max(scores)}")
    print(f"min(scores) = {min(scores)}")
    print(f"sorted(scores) = {sorted(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
