#!/usr/bin/env python3


class AchiAnalytics:
    @staticmethod
    def common_achievements(achievements_lists):
        all_achievements = [achievement for achievement in achievements_lists]
        common = set.intersection(*all_achievements)
        return common

    @staticmethod
    def unique_achievements(achievements_lists):
        all_achievements = [achievement for achievement in achievements_lists]
        unique = set()
        for achievement in set.union(*all_achievements):
            count = sum(1 for ach in all_achievements if achievement in ach)
            if count == 1:
                unique.add(achievement)
        return unique

    @staticmethod
    def all_unique_achievements(achievements_lists):
        all_achievements = [achievement for achievement in achievements_lists]
        all_achievements_set = set.union(*all_achievements)
        return all_achievements_set


def AchievementHunter():
    alice = {'first kill', 'level 10', 'treasure hunter', 'speed demon'}
    bob = {'first kill', 'level 10', 'boss slayer', 'collector'}
    charlie = {'level 10', 'treasure hunter', 'boss slayer', 'speed \
demon', 'perfectionist'}

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print()

    print("=== Achievement Analytics ===")
    print("All unique achievements:", end=" ")
    a_uni = AchiAnalytics.all_unique_achievements([alice, bob, charlie])
    print(a_uni)
    print("Total unique achievements:", end=" ")
    print(len(a_uni))

    print()
    print("Common to all players:", end=" ")
    com_ach = AchiAnalytics.common_achievements([alice, bob, charlie])
    print(com_ach)
    print("Rare achievements (1 player):", end=" ")
    rare = AchiAnalytics.unique_achievements([alice, bob, charlie])
    print(rare)

    print()
    print("Alice vs Bob common:", end=" ")
    print(AchiAnalytics.common_achievements([alice, bob]))
    commab = AchiAnalytics.all_unique_achievements([alice, bob])
    print("Alice unique:", end=" ")
    print(commab.difference(bob))
    print("Bob unique:", end=" ")
    print(commab.difference(alice))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    AchievementHunter()
