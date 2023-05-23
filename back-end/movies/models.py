from django.db import models
from django.conf import settings
from accounts.models import Accounts
# Create your models here.


class AllMovie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adult = models.BooleanField()
    backdrop_path = models.URLField(null=True)
    # genre_ids = models.ForeignKey(AllGenre, on_delete=models.CASCADE)
    # genre_ids = models.ManyToManyField(AllGenre)
    movie_id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=10)
    overview = models.TextField()
    popularity = models.DecimalField(max_digits=100000, decimal_places=4)
    poster_path = models.URLField(max_length=200)
    release_date = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    vote_average = models.DecimalField(max_digits=10, decimal_places=3)
    vote_count = models.IntegerField(default=0)
    eng_title = models.CharField(max_length=500)

class AllGenre(models.Model):
    # genre = models.AutoField(primary_key=True)
    movie = models.ForeignKey("AllMovie", on_delete=models.CASCADE)
    genre_ids = models.CharField(max_length=50, null=True)
    
class AllRelatedVideo(models.Model):
    # vide = models.AutoField(primary_key=True)
    movie = models.ForeignKey("AllMovie", on_delete=models.CASCADE)
    video = models.URLField(max_length=200, null=True)


class TodayMovie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adult = models.BooleanField()
    backdrop_path = models.URLField(null=True)
    # genre_ids = models.ForeignKey(AllGenre, on_delete=models.CASCADE)
    # genre_ids = models.ManyToManyField(AllGenre)
    movie_id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=10)
    overview = models.TextField()
    popularity = models.DecimalField(max_digits=100000, decimal_places=4)
    poster_path = models.URLField(max_length=200)
    release_date = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    vote_average = models.DecimalField(max_digits=10, decimal_places=3)
    vote_count = models.IntegerField(default=0)
    eng_title = models.CharField(max_length=500)

class TodayGenre(models.Model):
    movie = models.ForeignKey("TodayMovie", on_delete=models.CASCADE)
    genre_ids = models.CharField(max_length=50)

class TodayRelatedVideo(models.Model):
    movie = models.ForeignKey("TodayMovie", on_delete=models.CASCADE)
    video = models.URLField(max_length=200, null=True)
    
    
class TodayMovieCreated(models.Model):
    today = models.DateTimeField(auto_now=True)
    
class MovieDetail(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    # movie = models.ForeignKey(AllMovie, on_delete=models.CASCADE)
    budget = models.BigIntegerField(null=True)
    revenue = models.BigIntegerField(null=True)
    tagline = models.TextField(null=True)
    adult = models.BooleanField(null=True)
    backdrop_path = models.URLField(null=True)
    homepage = models.URLField(null=True)
    original_title = models.CharField(max_length=20, null=True)
    overview = models.TextField(null=True)
    popularity = models.DecimalField(max_digits=100000, decimal_places=3, default=0)
    poster_path = models.URLField(null=True)
    release_date = models.DateField(null=True)
    runtime = models.IntegerField(null=True)
    vote_average = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    

class ActorList(models.Model):
    actor = models.IntegerField(primary_key=True)
    actor_id = models.IntegerField()
    actor_name = models.CharField(max_length=1000)
    actor_popularity = models.DecimalField(max_digits=1000000, decimal_places=4, default = 0)
    actor_revenue = models.DecimalField(max_digits=1000000, decimal_places=4, default = 0)
    

class Comment(models.Model):
    movie = models.ForeignKey(AllMovie, on_delete=models.CASCADE)
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    star_score = models.FloatField(null=True)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    user_profile_img = models.ImageField(upload_to='comment_profile_images/', null=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
