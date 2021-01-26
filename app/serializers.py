from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    created_by_user = serializers.CharField(source='created_by.full_name', read_only=True)

    class Meta:
        model = Comment
        fields = ('article', 'text', 'created_by_user', 'created_on', 'id')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        user = self.context.get('request').user

        validated_data['created_by'] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        instance.modified_by = user

        return super().update(instance, validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    created_by_user = serializers.CharField(source='created_by.full_name', read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'slug', 'content', 'comments', 'created_by_user', 'created_on', 'id')
        extra_kwargs = {
            'slug': {'read_only': True},
        }

    def create(self, validated_data):
        user = self.context.get('request').user

        validated_data['created_by'] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        instance.modified_by = user

        return super().update(instance, validated_data)


