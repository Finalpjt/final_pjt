from rest_framework import serializers
from .models import AllGenre, AllMovie, AllRelatedVideo, TodayGenre, TodayMovie, TodayRelatedVideo, Comment



class AllGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllGenre
        fields = ('genre_ids',)

class AllVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllRelatedVideo
        # fields = ('id', 'title', 'content')
        # fields = ('id', 'title', 'content', 'user', 'username')
        # fields = '__all__'
        fields = ('video',)
        
class AllMovieListSerializer(serializers.ModelSerializer):
    genres = AllGenreSerializer(many=True, read_only=True, source='allgenre_set')
    videos = AllVideoListSerializer(many=True, read_only=True, source='allrelatedvideo_set')
    # print(videos)
    # print(genres)
    class Meta:
        model = AllMovie
        # fields = ('movie_id', 'adult', 'original_language', 'genres', 'videos')
        fields = '__all__'
        
class TodayGenreSerializer(serializers.ModelSerializer):
    # genre_ids = serializers.SerializerMethodField()
    class Meta:
        model = AllGenre
        fields = ('genre_ids',) 
        

class TodayVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayRelatedVideo
        fields = ('video',)

class TodayMovieListSerializer(serializers.ModelSerializer):
    genre_ids = TodayGenreSerializer(many=True, read_only=True, source='todaygenre_set')
    # genre_ids = serializers.SerializerMethodField()
    videos = TodayVideoListSerializer(many=True, read_only=True, source='todayrelatedvideo_set')
    class Meta:
        model = TodayMovie
        fields = '__all__'
        



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
        model = AllMovie
        fields = '__all__'
        # read_only_fields = ('user', )