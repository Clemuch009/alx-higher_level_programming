import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description = "returns a greeting")


    def resolve_hello(self, info):
        return "Hello Muchai! Your first GraphQL response."

schema = graphene.Schema(query=Query)


