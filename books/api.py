from .models import Book
from rest_framework import viewsets, permissions
from .serializers import BookSerializer
from .permissions import IsAuthenticatedOwnerOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOwnerOrReadOnly]
    serializer_class = BookSerializer


# class MyLibViewSet(viewsets.ModelViewSet):
#     serializer_class = BookSerializer
#     permission_classes = [IsOwner, ]
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Book.objects.filter(owner=self.request.user)
#
#         return Book.objects.filter(pk=pk)
