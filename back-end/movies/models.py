from django.db import models
from django.conf import settings

# Create your models here.


class AllMovie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adult = models.BooleanField()
    backdrop_path = models.TextField(null=True)
    # genre_ids = models.ForeignKey(AllGenre, on_delete=models.CASCADE)
    # genre_ids = models.ManyToManyField(AllGenre)
    movie_id = models.IntegerField()
    original_language = models.CharField(max_length=10)
    overview = models.TextField()
    popularity = models.BigIntegerField()
    # popularity = models.DecimalField(max_digits=100000, decimal_places=3)
    # poster_path = models.URLField(max_length=200)
    poster_path = models.TextField(max_length=200)
    release_date = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    vote_average = models.DecimalField(max_digits=10, decimal_places=3)
    vote_count = models.IntegerField(default=0)
    eng_title = models.CharField(max_length=500)

# class AllGenre(models.Model):
#     movie_id = models.ForeignKey(AllMovie, on_delete=models.CASCADE)
#     genre_ids = models.CharField(max_length=50)
    
# class AllRelatedVideo(models.Model):
#     movie_id = models.ForeignKey(AllMovie, on_delete=models.CASCADE)
#     video = models.URLField(max_length=200)


# class TodayMovie(models.Model):
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     adult = models.BooleanField()
#     backdrop_path = models.TextField(null=True)
#     # genre_ids = models.TextField(max_length=100)
#     movie_id = models.IntegerField()
#     original_language = models.CharField(max_length=10)
#     overview = models.TextField()
#     popularity = models.DecimalField(max_digits=100000, decimal_places=3)
#     poster_path = models.URLField(max_length=200)
#     release_date = models.DateField()
#     title = models.CharField(max_length=100)
#     vote_average = models.DecimalField(max_digits=10, decimal_places=3)
#     vote_count = models.IntegerField(default=0)
#     eng_title = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class TodayGenre(models.Model):
#     movie_id = models.ForeignKey(TodayMovie, on_delete=models.CASCADE)
#     genre_ids = models.CharField(max_length=50)

# class TodayRelatedVideo(models.Model):
#     movie_id = models.ForeignKey(TodayMovie, on_delete=models.CASCADE)
#     videos = models.URLField(max_length=200)

# class Comment(models.Model):
#     movie_id = models.ForeignKey(AllMovie, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
