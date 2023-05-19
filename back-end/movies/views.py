from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import AllMovieListSerializer, AllVideoListSerializer, AllGenreSerializer, CommentSerializer
from .serializers import TodayMovieListSerializer, TodayVideoListSerializer, TodayGenreSerializer
from .models import AllGenre, TodayGenre, AllMovie, AllRelatedVideo, TodayMovie, TodayRelatedVideo, Comment



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
    if request.method == 'GET':
        movies = get_list_or_404(TodayMovie)
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