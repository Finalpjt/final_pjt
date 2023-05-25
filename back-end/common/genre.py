import requests
import json
from django.conf import settings

def f_my_api_key():
        my_api_key = getattr(settings, 'TMDB_SECRET_KEY', 'TMDB_SECRET_KEY')
        return my_api_key

my_api_key = f_my_api_key()
genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + my_api_key
genre_res = requests.get(genre_url).text
genre_list = json.loads(genre_res)['genres']
print(genre_list)
for genre_set in genre_list:
    print(genre_set['name'])