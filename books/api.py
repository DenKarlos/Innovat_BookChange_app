from .models import Book
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer
from .permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response

from .servises import BookFilter


class BooksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer

    # @action(methods=['get'], detail=False)
    # def mylib(self, request):
    #     mylib = Book.objects.filter(owner=request.user)
    #     serializer = self.get_serializer(mylib, many=True)
    #     return Response(serializer.data)
    #
    # @action(methods=['get'], detail=False)
    # def another(self, request):
    #     another = Book.objects.exclude(owner=request.user)
    #     serializer = self.get_serializer(another, many=True)
    #     return Response(serializer.data)


class MyLibViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return self.request.user.books.all().filter(is_ordered=False)
        # Book.objects.filter(owner=self.request.user).filter(is_ordered=False)

        return self.request.user.books.filter(is_ordered=False).filter(pk=pk)
            # Book.objects.filter(owner=self.request.user).filter(is_ordered=False).filter(pk=pk)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AnotherBooksViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = BookFilter
    # filter_fields = ['publication_year',]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Book.objects.exclude(owner=self.request.user).filter(is_ordered=False)

        return Book.objects.exclude(owner=self.request.user).filter(is_ordered=False).filter(pk=pk)