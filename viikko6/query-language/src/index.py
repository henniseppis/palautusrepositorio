from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or, QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    #matcher = query.build()
    matcher = query.playsIn("NYR").build()


    for player in stats.matches(matcher):
        print(player)

#    matcher = And(
#    HasFewerThan(2, "goals"),
#    PlaysIn("NYR")
#)
#
#    matcher1 = And(
#    Not(HasAtLeast(2, "goals")),
#    PlaysIn("NYR")
#)
    
    #matcher = And(
    #HasAtLeast(70, "points"),
    #Or(
    #    PlaysIn("NYR"),
    #    PlaysIn("FLA"),
    #    PlaysIn("BOS")
    #)
#)#
#

    
    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))
#
#
#
    #matcher = And(c
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(20, "assists"),
    #    PlaysIn("PHI")
    #)
    #for player in stats.matches(matcher):
    #    print(player)
    
    #for player in stats.matches(matcher):
    #    print(player)
#

if __name__ == "__main__":
    main()
