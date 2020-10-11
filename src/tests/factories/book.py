from book.models import Author, Book

import factory


__all__ = [
    'AuthorFactory', 'BookFactory',
]


class AuthorFactory(factory.DjangoModelFactory):

    class Meta:
        model = Author

    date_of_birth = factory.Faker('date_object')


class BookFactory(factory.DjangoModelFactory):
    author = factory.SubFactory(AuthorFactory)
    title = 'Book Title'
    publish_year = 1992

    class Meta:
        model = Book
