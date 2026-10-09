from rest_framework.routers import DefaultRouter

from .views import (BookViewSet, CommentViewSet)

router = DefaultRouter()


router.register('books', BookViewSet)
router.register('comments', CommentViewSet)


urlpatterns = router.urls

