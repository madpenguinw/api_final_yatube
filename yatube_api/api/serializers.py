from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Group, Post, Comment, Follow


User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    def validate(self, data):
        if (
            self.context['request'].method == 'POST'
            and data['user'] == data['following']
        ):
            raise serializers.ValidationError(
                'Ошибка: обнаружена попытка подписаться на самого себя'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following', 'user'],
            )
        ]
