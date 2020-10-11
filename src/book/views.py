from book.models import Author, Book
from book.serializers import AuthorSerializer, BookSerializer

from django.utils import timezone

from rest_framework import generics, status
from rest_framework.response import Response


class AuthorsView(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by('-id')
    serializer_class = AuthorSerializer
    ordering = ('-id', )

    def perform_create(self, serializer):
        serializer.save(
            created_by_student=timezone.now(),
        )


class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.created_by_student:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Cannot delete Author created by system'},
                        status=status.HTTP_400_BAD_REQUEST)


class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by_student=timezone.now(),
        )


class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.created_by_student:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Cannot delete Book created by system'},
                        status=status.HTTP_400_BAD_REQUEST)
