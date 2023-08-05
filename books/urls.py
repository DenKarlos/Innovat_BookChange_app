from rest_framework import routers
from .api import BookViewSet

router = routers.DefaultRouter()
# router_2 = routers.DefaultRouter()
router.register('api/books', BookViewSet, 'books')
# router_2.register('api/mylib', MyLibViewSet, 'mylib')

urlpatterns = router.urls
