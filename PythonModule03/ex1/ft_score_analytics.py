#!/usr/bin/env python3


import sys


def ft_score_analytics():
    scores = []
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py \
<score1> <score2> ...")
        return
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Warning: Invalid score '{arg}'. Ignored.")

    print("Scores processed:", scores)
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
