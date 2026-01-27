#!/usr/bin/env python3


class AchievementHunter:
    def __init__(self, name):
        self.name = name
        self.achievements = set()

    def add_achievement(self, achievement):
        self.achievements.add(achievement)

    def add_list_of_achievements(self, achievements):
        for achievement in achievements:
            self.add_achievement(achievement)

    def list_achievements(self):
        if not self.achievements:
            print(f"{self.name} has no achievements yet.")
        else:
            print(f"{self.name}'s Achievements:", end=" ")
            print(", ".join(f"'{a}'" for a in self.achievements))


class AchievementAnalytics:
    @staticmethod
    def common_achievements(hunters):
        all_achievements = [hunter.achievements for hunter in hunters]
        common = set.intersection(*all_achievements)
        return common

    @staticmethod
    def unique_achievements(hunters):
        all_achievements = [hunter.achievements for hunter in hunters]
        unique = set()
        for achievement in set.union(*all_achievements):
            count = sum(1 for ach in all_achievements if achievement in ach)
            if count == 1:
                unique.add(achievement)
        return unique

    @staticmethod
    def all_achievements(hunters):
        all_achievements = [hunter.achievements for hunter in hunters]
        all_achievements_set = set.union(*all_achievements)
        return all_achievements_set

    @staticmethod
    def common_achievements_(achievements_lists):
        all_achievements = [achievement for achievement in achievements_lists]
        common = set.intersection(*all_achievements)
        return common

    @staticmethod
    def unique_achievements_(achievements_lists):
        all_achievements = [achievement for achievement in achievements_lists]
        unique = set()
        for achievement in set.union(*all_achievements):
            count = sum(1 for ach in all_achievements if achievement in ach)
            if count == 1:
                unique.add(achievement)
        return unique

    @staticmethod
    def all_achievements_(achievements_lists):
        all_achievements = [achievement for achievement in achievements_lists]
        all_achievements_set = set.union(*all_achievements)
        return all_achievements_set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    alice = AchievementHunter("Alice")
    alice.add_list_of_achievements(['first kill', 'level 10', 'treasure \
hunter', 'speed demon'])
    bob = AchievementHunter("Bob")
    bob.add_list_of_achievements(['first kill', 'level 10', 'boss \
slayer', 'collector'])
    charlie = AchievementHunter("Charlie")
    charlie.add_list_of_achievements(['level 10', 'treasure hunter', 'boss \
slayer', 'speed demon', 'perfectionist'])

    alice.list_achievements()
    bob.list_achievements()
    charlie.list_achievements()
    print()

    print("=== Achievement Analytics ===")
    print("All unique achievements:", end=" ")
    print(AchievementAnalytics.all_achievements([alice, bob, charlie]))
    print("Total unique achievements:", end=" ")
    print(len(AchievementAnalytics.all_achievements([alice, bob, charlie])))

    print()
    print("Common to all players:", end=" ")
    print(AchievementAnalytics.common_achievements([alice, bob, charlie]))
    print("Rare achievements (1 player):", end=" ")
    print(AchievementAnalytics.unique_achievements([alice, bob, charlie]))

    print()
    print("Alice vs Bob common:", end=" ")
    print(AchievementAnalytics.common_achievements([alice, bob]))
    all = AchievementAnalytics.all_achievements([alice, bob])
    print("Alice unique:", end=" ")
    print(AchievementAnalytics.unique_achievements_([all, bob.achievements]))
    print("Bob unique:", end=" ")
    print(AchievementAnalytics.unique_achievements_([all, alice.achievements]))
