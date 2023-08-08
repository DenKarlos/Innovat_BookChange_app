from .models import Book
from rest_framework import viewsets, permissions
from rest_framework import permissions
from .serializers import BookSerializer
from .permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response


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
            return Book.objects.filter(owner=self.request.user).filter(is_ordered=False)

        return Book.objects.filter(pk=pk)


class AnotherBooksViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Book.objects.exclude(owner=self.request.user).filter(is_ordered=False)

        return Book.objects.filter(pk=pk)