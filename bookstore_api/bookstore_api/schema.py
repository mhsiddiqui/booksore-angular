import graphene

import book_service.schema as book_service_schema


class Query(book_service_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(book_service_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,mutation=Mutation)
