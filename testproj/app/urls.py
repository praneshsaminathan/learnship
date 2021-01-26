from testproj.utils.apps import get_api_url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet


router = DefaultRouter(trailing_slash=True)
router.register(r'articles', ArticleViewSet, 'api-articles')
router.register(r'comments', CommentViewSet, 'api-comments')

urlpatterns = [
    path(get_api_url(), include(router.urls)),

]

