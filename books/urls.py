from rest_framework import routers
from .api import BooksViewSet, MyLibViewSet, AnotherBooksViewSet

router_1 = routers.DefaultRouter()
router_2 = routers.DefaultRouter()
router_3 = routers.DefaultRouter()
router_1.register('api/books', BooksViewSet, 'books')
router_2.register('api/mylib', MyLibViewSet, 'mylib')
router_3.register('api/another', AnotherBooksViewSet, 'another')


urlpatterns = router_1.urls + router_2.urls + router_3.urls
