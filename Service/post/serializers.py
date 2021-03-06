from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from post.models import Article, Category, ArticleFavorite
from post.utils import GeoNotFoundException, get_ip_area
from user.serializers import UserSerializer


# class CommentSerializer(ReadCommentSerializer):
#     user = UserSerializer(read_only=True)
#
#     class Meta(ReadCommentSerializer.Meta):
#         fields = ('id', 'user', 'user_moderator',
#                   'permalink', 'comment', 'submit_date',
#                   'parent_id', 'level', 'is_removed', 'allow_reply', 'flags')


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)
    cate_name = serializers.ReadOnlyField(source='cate.name')

    class Meta:
        model = Article
        fields = ('url', 'id', 'title', 'cate', 'cate_name', 'thumbnail', 'author',
                  'content', 'created', 'updated')


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)
    favor = serializers.SerializerMethodField()
    cate_name = serializers.ReadOnlyField(source='cate.name')
    # comments = serializers.SerializerMethodField()
    # location = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('url', 'id', 'title', 'cate', 'cate_name', 'thumbnail', 'author', 'favor',
                  'content', 'created', 'updated')
    #
    # @staticmethod
    # def get_location(obj):
    #     try:
    #         location = get_ip_area(obj.ip_address)
    #         return location['country'] + location['region']
    #     except:
    #         return '火星'

    # def get_comments(self, obj):
    #     content_type = ContentType.objects.get_for_model(obj.__class__)
    #     qs = XtdComment.objects.filter(content_type=content_type,
    #                                    object_pk=obj.pk,
    #                                    site__pk=settings.SITE_ID,
    #                                    is_public=True)[:10]
    #     comments = CommentSerializer(qs, many=True, context=self.context).data
    #     return comments

    def get_favor(self, obj):
        user = self.context['request'].user.pk
        qs = ArticleFavorite.objects.filter(post=obj.pk, user=user)
        if qs is not None and qs.count() > 0:
            return True
        return False


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name', 'created')


class ArticleFavoriteSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer(read_only=True)

    class Meta:
        model = ArticleFavorite
        fields = ('user', 'post', 'created')


class ArticleFavoriteAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleFavorite
        fields = ('user', 'post')
