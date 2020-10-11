from book.models import Author, Book

import factory


__all__ = [
    'AuthorFactory', 'BookFactory',
]


class AuthorFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Author

    date_of_birth = factory.Faker('date_object')


class BookFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(AuthorFactory)
    title = 'Book Title'
    publish_year = 1992

    class Meta:
        model = Book
