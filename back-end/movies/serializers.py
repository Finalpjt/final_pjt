from rest_framework import serializers
from .models import AllGenre, AllMovie, AllRelatedVideo, TodayMovie, TodayRelatedVideo, Comment

class AllGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllGenre
        fields = '__all__'

class AllMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllMovie
        # fields = ('id', 'title', 'content')
        # fields = ('id', 'title', 'content', 'user', 'username')
        fields = '__all__'

class AllVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllRelatedMovie
        # fields = ('id', 'title', 'content')
        # fields = ('id', 'title', 'content', 'user', 'username')
        fields = '__all__'

class TodayMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayMovie
        fields = '__all__'

class TodayVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayRelatedVideo
        fields = '__all__'


# class MovieListSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Movie
#         # fields = ('id', 'title', 'content')
#         fields = ('id', 'title', 'content', 'user', 'username')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('user', )