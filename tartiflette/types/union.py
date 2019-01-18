from typing import List, Optional

from tartiflette.types.type import GraphQLType


class GraphQLUnionType(GraphQLType):
    """
    Union Type Definition

    When a field can return one of a heterogeneous set of types, a Union
    type is used to describe what types are possible as well as providing
    a function to determine which type is actually used when the field
    if resolved.
    """

    def __init__(
        self,
        name: str,
        gql_types: List[GraphQLType],
        description: Optional[str] = None,
        schema=None,
    ):
        super().__init__(name=name, description=description, schema=schema)
        self.gql_types = gql_types
        self._possible_types = []

    def __repr__(self) -> str:
        return "{}(name={!r}, gql_types={!r}, description={!r})".format(
            self.__class__.__name__,
            self.name,
            self.gql_types,
            self.description,
        )

    def __eq__(self, other) -> bool:
        return super().__eq__(other) and self.gql_types == other.gql_types

    # Introspection Attribute
    @property
    def kind(self):
        return "UNION"

    @property
    def is_union(self):
        return True

    @property
    def possibleTypes(self):
        return self._possible_types

    def bake(self, schema, custom_default_resolver):
        super().bake(schema, custom_default_resolver)
        self._possible_types = [
            self._schema.find_type(x) for x in self.gql_types
        ]
