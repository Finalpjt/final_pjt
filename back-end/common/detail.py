def movie_detail_url(movie_id):
    import pandas as pd
    import json
    import requests
    
    my_api_key = '6a5ece7778e61cb35c55c953b8743b0d'
    url = 'https://api.themoviedb.org/3/movie/'+ str(movie_id) +'?api_key=' + my_api_key + '&language=ko-KR'
    res = requests.get(url).text
    data = json.loads(res)
    # print(data)
    data['backdrop_path'] = 'https://image.tmdb.org/t/p/original' + data['backdrop_path']
    data['poster_path'] = 'https://image.tmdb.org/t/p/original' + data['poster_path']
    for idx, genre in enumerate(data['genres']):
        data['genres'][idx] = genre['name']
    new_data = [
        {
            'movie_id': data['id'],
            'budget': data['budget'],
            'revenue': data['revenue'],
            'tagline': data['tagline'],
        }
    ]
    
    return new_data