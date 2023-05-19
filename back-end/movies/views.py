from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.db import connections
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import AllMovieListSerializer, AllVideoListSerializer, AllGenreSerializer, CommentSerializer
from .serializers import TodayMovieListSerializer, TodayVideoListSerializer, TodayGenreSerializer
from .models import AllGenre, TodayGenre, AllMovie, AllRelatedVideo, TodayMovie, TodayRelatedVideo, Comment, TodayMovieCreated

from common.todaymovie import get_today_movie_list
from datetime import date, datetime, timedelta
import json


def delete_yesterday():
    movie_list = TodayMovie.objects.all()
    for movie in movie_list:
        movie.delete()
    video_list = TodayRelatedVideo.objects.all()
    for video in video_list:
        video.delete()
    genre_list = TodayGenre.objects.all()
    for genre in genre_list:
        genre.delete()

def today_json_to_db():
    ymd = date.today() - timedelta(1)
    ymd = datetime.strftime(ymd, '%Y%m%d')
    today = ymd
    with open('./movies/fixtures/{}_movie.json'.format(today), 'r', encoding='UTF-8') as f:
        today_movie_js = json.loads(f.read()) ## json 라이브러리 이용

    with open('./movies/fixtures/{}_video.json'.format(today)) as f:
        today_video_js = json.loads(f.read()) ## json 라이브러리 이용

    with open('./movies/fixtures/{}_genre.json'.format(today)) as f:
        today_genre_js = json.loads(f.read()) ## json 라이브러리 이용

    today_movie_list = today_movie_js
    today_video_list = list(today_video_js)
    today_genre_list = list(today_genre_js)
    
    for movie in today_movie_list:
        # Movie 모델 필드명에 맞추어 데이터를 저장함.
        movie_list = TodayMovie()
        movie = movie['fields']
        movie_list.adult = movie['adult']
        movie_list.backdrop_path = movie['backdrop_path']
        movie_list.movie_id = movie['movie_id']
        movie_list.original_language = movie['original_language']
        movie_list.overview = movie['overview']
        movie_list.popularity = movie['popularity']
        movie_list.poster_path = movie['poster_path']
        movie_list.release_date = movie['release_date']
        movie_list.title = movie['title']
        movie_list.vote_average = movie['vote_average']
        movie_list.vote_count = movie['vote_count']
        movie_list.eng_title = movie['eng_title']
        movie_list.save()
    
    for videos in today_video_list:
        video_list = TodayRelatedVideo()
        videos = videos['fields']
        video_list.movie_id = videos['movie_id']
        video_list.video = videos['video']
        video_list.save()
        
    for genres in today_genre_list:
        genre_list = TodayGenre()
        genres = genres['fields']
        genre_list.movie_id = genres['movie_id']
        genre_list.genre_ids = genres['genre_ids']
        genre_list.save()
    
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(AllMovie)
        serializer = AllMovieListSerializer(movies, many=True)
        for iidx in range(len(serializer.data)):
            genre_list, video_list = [], []
            for genre in dict(serializer.data[iidx])['genres']:
                genre_list.append(dict(genre)['genre_ids'])
            for idx, i in enumerate(genre_list):
                serializer.data[iidx]['genres'][idx] = i
                
            for video in dict(serializer.data[iidx])['videos']:
                video_list.append(dict(video))
            for v_idx, v in enumerate(video_list):
                serializer.data[iidx]['videos'][v_idx] = v['video']
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AllMovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def today_movie_list(request):
    # get_today_movie_list()
    TodayMovieCreated.objects.today = datetime.now()
    ymd = date.today()
    today_ymd = datetime.strftime(ymd, '%Y-%m-%d')
    days, is_created = TodayMovieCreated.objects.get_or_create()
    if is_created:
        delete_time = TodayMovieCreated.objects.all()
        for x in delete_time:
            x.delete()
        days, is_created = TodayMovieCreated.objects.get_or_create()
        # new_time = TodayMovieCreated()
        # new_time.today = today_ymd
        days.today = today_ymd
        get_today_movie_list()
        today_json_to_db()
        print(ymd)
        print(today_ymd)
        print(is_created)
        print(days.today)
    else:
        print(str(days.today)[:10])
        # delete_time = TodayMovieCreated.objects.all()
        # for x in delete_time:
        #     x.delete()
        # days, is_created = TodayMovieCreated.objects.get_or_create()
        if today_ymd != str(days.today)[:10]:
            delete_yesterday()
            delete_time = TodayMovieCreated.objects.all()
            for x in delete_time:
                x.delete()
            days, is_created = TodayMovieCreated.objects.get_or_create()
            # new_time = TodayMovieCreated()
            # new_time.today = today_ymd
            get_today_movie_list()
            today_json_to_db()
            
    if request.method == 'GET':
        movies = get_list_or_404(TodayMovie)
        # print(movies)
        serializer = TodayMovieListSerializer(movies, many=True)
        for iidx in range(len(serializer.data)):
            genre_list, video_list = [], []
            for genre in dict(serializer.data[iidx])['genre_ids']:
                genre_list.append(dict(genre)['genre_ids'])
            for idx, i in enumerate(genre_list):
                serializer.data[iidx]['genre_ids'][idx] = i
            
            for video in dict(serializer.data[iidx])['videos']:
                video_list.append(dict(video))
            for v_idx, v in enumerate(video_list):
                serializer.data[iidx]['videos'][v_idx] = v['video']
                
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodayMovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_id):
    # movie = Movie.objects.get(pk=movie_id)
    movie = get_object_or_404(AllMovie, pk=movie_id)

    if request.method == 'GET':
        serializer = AllMovieListSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = AllMovieListSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def today_movie_detail(request, movie_id):
    movie = get_object_or_404(TodayMovie, pk=movie_id)

    if request.method == 'GET':
        serializer = TodayMovieListSerializer(movie)
        genre_list = []
        for genre in serializer.data['genre_ids']:
            genre_list.append(dict(genre)['genre_ids'])
        for idx, i in enumerate(genre_list):
            serializer.data['genre_ids'][idx] = i
        
        video_list = []
        for video in serializer.data['videos']:
            video_list.append(dict(video))
        for v_idx, v in enumerate(video_list):
            serializer.data['videos'][v_idx] = v['video']
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = TodayMovieListSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['POST'])
def comment_create(request, movie_pk):
    # movie = Movie.objects.get(pk=Movie_pk)
    movie = get_object_or_404(AllMovie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(Movie=Movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)