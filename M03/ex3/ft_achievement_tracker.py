def achievement_analytics(alice: set[str], bob: set[str],
                          charlie: set[str]) -> None:
    print("=== Achievement Analytics ===\n")
    achievements: set[str] = alice.union(bob, charlie)
    print("All unique achievements:", achievements)
    print("Total unique achievements:", len(achievements))
    print("\nCommon to all players:", alice.intersection(bob, charlie))
    shared_by_two_or_more = (alice & bob) | (bob & charlie) | (charlie & alice)
    rare_achievements = achievements - shared_by_two_or_more
    print("Rare achievements (only one player):",
          rare_achievements)
    print("\nAlice vs Bob common:", (alice & bob))
    print("Alice unique:", alice - (bob | charlie))
    print("Bob unique:", bob - (alice | charlie))


def achievement_tracker():
    print("=== Achievement Tracker System ===\n")
    alice_achivements = set(
        ["first_kill", "level_10", "treasure_hunter", "speed_demon"]
    )
    bob_achievements = set(["first_kill", "level_10",
                            "boss_slayer", "collector"])
    charlie_achievements = set(
        ["level_10", "treasure_hunter",
         "boss_slayer", "speed_demon", "perfectionist"]
    )
    print("Player Alice achievements:", alice_achivements)
    print("Player Bob achievements:", bob_achievements)
    print("Player Charlie achievements:", charlie_achievements,
          end='\n\n')
    achievement_analytics(alice_achivements, bob_achievements,
                          charlie_achievements)


if __name__ == "__main__":
    achievement_tracker()
