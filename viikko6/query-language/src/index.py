from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher_with_query_builder = (
        query
            .plays_in("NYR")
            .has_at_least(10, "goals")
            .has_fewer_than(20, "goals")
            .build()
    )

    matcher_with_direct_conditions = And(
        PlaysIn("NYR"),
        HasAtLeast(10, "goals"),
        HasFewerThan(20, "goals")
    )

    # Näissä pitäisi olla sama lopputulos

    for player in stats.matches(matcher_with_query_builder):
        print(player)

    print()

    for player in stats.matches(matcher_with_direct_conditions):
        print(player)

    print()

    m1 = (
        query
            .plays_in("PHI")
            .has_at_least(10, "assists")
            .has_fewer_than(5, "goals")
            .build()
    )

    m2 = (
        query
            .plays_in("EDM")
            .has_at_least(50, "points")
            .build()
    )

    matcher_with_helper_variables = query.one_of(m1, m2).build()

    matcher_without_helper_variables = (
        query
            .one_of(
                query
                    .plays_in("PHI")
                    .has_at_least(10, "assists")
                    .has_fewer_than(5, "goals")
                    .build(),
                query
                    .plays_in("EDM")
                    .has_at_least(50, "points")
                    .build()
            )
            .build()
    )

    

    # Näissäkin lopputuloksen pitäisi olla sama

    for player in stats.matches(matcher_without_helper_variables):
        print(player)

    print()

    for player in stats.matches(matcher_with_helper_variables):
        print(player)


if __name__ == "__main__":
    main()
