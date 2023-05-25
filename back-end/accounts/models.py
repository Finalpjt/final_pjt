from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import json
import requests

# Create your models here.
# my_api_key = '6a5ece7778e61cb35c55c953b8743b0d'
# genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + my_api_key
# genre_res = requests.get(genre_url).text
# genre_list = json.loads(genre_res)['genres']

class Accounts(AbstractUser):
    my_api_key = '6a5ece7778e61cb35c55c953b8743b0d'
    genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + my_api_key
    genre_res = requests.get(genre_url).text
    genre_list = json.loads(genre_res)['genres']
    GENRE_CHOICES = []
    for genre_set in genre_list:
        # print(genre_set['name'])
        GENRE_CHOICES.append((genre_set['name'], genre_set['name']))
    genres = models.CharField(
        max_length=255,
        choices=GENRE_CHOICES,
        default='Actions',
    )
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(max_length=255)
    profile_img = ProcessedImageField(
        upload_to='profile_images/', 
        null=True,
        blank=True,
        processors=[ResizeToFill(100,100)],
        options={'quality':70},
        )
    
    def __str__(self):
        return self.username