import graphene
from models import Book
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class BookQuery(object):
    book = graphene.Field(BookType, id=graphene.Int(), name=graphene.String())
    title = graphene.Field(BookType, id=graphene.String(), name=graphene.String())
    user = graphene.List(UserType)
    books = graphene.List(BookType)

    # def resolve_title(self, info, **kwargs):
    #     return
    #
    # def resolve_user(self, info, **kwargs):
    #     return get_user_model().objects.all()

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Book.objects.get(pk=id)

        return None

    def resolve_books(self, info, **kwargs):
        return Book.objects.all().order_by('id')
