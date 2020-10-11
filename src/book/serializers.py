from book.models import Author, Book

from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'date_of_death',
            'email',
            'country',
            'gender',
            'language',
            'created_by_student',
        )
        read_only_fields = ('created_by_student', )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'authors',
            'author',
            'title',
            'publish_year',
            'created_by_student',
        )
        read_only_fields = ('created_by_student', )
        write_only_fields = ('author', )
