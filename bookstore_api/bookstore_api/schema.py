import graphene
import graphql_jwt
import book_service.schema as book_service_schema
import user_service.schema as user_service_schema


class BookServiceQuery(book_service_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class BookServiceMutation(book_service_schema.Mutation, graphene.ObjectType):
    pass


class UserServiceQuery(user_service_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class UserServiceMutation(user_service_schema.Mutation, graphene.ObjectType):
    pass


class AuthServiceMutations(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class AllSchemas(object):
    book_service = graphene.Schema(query=BookServiceQuery, mutation=BookServiceMutation)
    user_service = graphene.Schema(query=UserServiceQuery, mutation=UserServiceMutation)
    auth_service = graphene.Schema(mutation=AuthServiceMutations)