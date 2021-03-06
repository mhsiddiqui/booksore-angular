import graphene
from graphql_jwt.decorators import login_required

from models import Book
from graphene_django.types import DjangoObjectType


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class CreateBook(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    author = graphene.String()
    price = graphene.Float()

    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        author = graphene.String()
        price = graphene.Float()

    @login_required
    def mutate(self, info, title, description, author, price):
        return Book.objects.create(
            title=title, description=description, author=author, price=price
        )


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()


class Query(object):
    book = graphene.Field(BookType, id=graphene.Int(), name=graphene.String())
    books = graphene.List(BookType)

    @login_required
    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Book.objects.get(pk=id)

        return None

    @login_required
    def resolve_books(self, info, **kwargs):
        return Book.objects.all().order_by('id')
