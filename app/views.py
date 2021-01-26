from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from testproj.utils.permissions import IsSelfOrIsOwnerOrIsAdmin
from testproj.utils.serializer_mixin import GetSerializerClassMixin


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(mode='Active')
    permission_classes = (IsAuthenticated, )

    def get_permissions(self):

        if self.request.method not in ['GET']:
            self.permission_classes = (IsAuthenticated, IsSelfOrIsOwnerOrIsAdmin)
        return super(ArticleViewSet, self).get_permissions()

    @action(detail=False, methods=['get'], url_path='slug')
    def get_by_slug(self, request):
        slug = request.query_params.get('search')
        data = self.queryset.filter(slug=slug)
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Comment.objects.filter(mode='Active')

    def get_permissions(self):

        if self.request.method not in ['GET']:
            self.permission_classes = (IsAuthenticated, IsSelfOrIsOwnerOrIsAdmin)
        return super(CommentViewSet, self).get_permissions()


