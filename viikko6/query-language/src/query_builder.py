from matchers import All, And, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, query_object=All()):
        self.query_object = query_object

    def build(self):
        return self.query_object

    def plays_in(self, team):
        return QueryBuilder(And(self.query_object, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.query_object, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.query_object, HasFewerThan(value, attr)))

    def one_of(self, *query_objects):
        return QueryBuilder(Or(*query_objects))
