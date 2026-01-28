#!/usr/bin/env python3


class Player:
    def __init__(self, name, score, achiev, status, region):
        self.name = name
        self.score = score
        self.achiev = achiev
        self.status = status
        self.region = region


class ListAnalytics:
    def __init__(self, players):
        self.players = players

    def hight_score_players(self, threshold):
        yield [p.name for p in self.players if p.score > threshold]

    def active_players(self):
        yield [p.name for p in self.players if p.status == 'active']

    def score_doublers(self):
        yield [p.score * 2 for p in self.players]


class DictAnalytics:
    def __init__(self, players):
        self.players = players

    def player_scores(self):
        yield {p.name: p.score for p in self.players}

    def achievement_counts(self):
        yield {p.name: len(p.achiev) for p in self.players}

    def score_categories(self):
        yield {p.name: ('high' if p.score >= 2200 else 'low')
               for p in self.players}


class SetAnalytics:
    def __init__(self, players):
        self.players = players

    def unique_players(self):
        yield {p.name for p in self.players}

    def unique_achievements(self):
        unique = set()
        for p in self.players:
            unique = set(p.achiev).symmetric_difference(unique)
        yield unique

    def active_regions(self):
        yield {p.region for p in self.players if p.status == 'active'}


class CombinedAnalytics:
    def __init__(self, players):
        self.players = players

    def total_players(self):
        return len(self.players)

    def unique_achievements(self):
        all_achievements = set()
        for p in self.players:
            all_achievements.update(p.achiev)
        return all_achievements

    def average_score(self):
        total_score = sum(p.score for p in self.players)
        return total_score / len(self.players) if self.players else 0

    def top_performer(self):
        if not self.players:
            return None
        return max(self.players, key=lambda p: p.score).name


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    print()
    players = [
        Player('alice', 2300, ['first_kill', 'treasure_hunter'],
               status='active', region='north'),
        Player('bob', 1800, ['level_10', 'sharp_shooter'],
               status='active', region='east'),
        Player('charlie', 2150, ['sharp_shooter', 'treasure_hunter'],
               status='active', region='central'),
        Player('diana', 2050, ['boss_slayer', 'speed_runner', 'novice'],
               status='inactive', region='south'),
    ]

    print("=== List Comprehension Examples ===")
    analytics = ListAnalytics(players)
    high_scorers = list(analytics.hight_score_players(2000))
    print(f"High scorers (>2000): {high_scorers}")
    scores_doubled = list(analytics.score_doublers())
    print(f"Scores doubled: {scores_doubled}")
    active_players = list(analytics.active_players())
    print(f"Active players: {active_players}")
    print()

    print("=== Dict Comprehension Examples ===")
    analytics = DictAnalytics(players)
    players_scores = list(analytics.player_scores())
    print(f"Player scores: {players_scores}")
    scores_category = list(analytics.score_categories())
    print(f"Score categories: {scores_category}")
    achv_count = list(analytics.achievement_counts())
    print(f"Achievement counts: {achv_count}")
    print()

    print("=== Set Comprehension Examples ===")
    analytics = SetAnalytics(players)
    unique_players = list(analytics.unique_players())
    print(f"Unique players: {unique_players}")
    unique_achievements = list(analytics.unique_achievements())
    print(f"Unique achievements: {unique_achievements}")
    active_regions = list(analytics.active_regions())
    print(f"Active regions: {active_regions}")
    print()

    print("=== Combined Analysis ===")
    analytics = CombinedAnalytics(players)
    total_players = analytics.total_players()
    print(f"Total players: {total_players}")
    unique_achievements = analytics.unique_achievements()
    print(f"Unique achievements: {len(unique_achievements)}")
    avg_score = analytics.average_score()
    print(f"Average score: {avg_score}")
    top_player = analytics.top_performer()
    print(f"Top performer: {top_player}")
    print()
    print("=== End of Dashboard ===")
