import joblib


tv_shows = [
    {
        'name': 'The Good Doctor',
        'imdb_id': 6470478,
        'folder': 'Z:/Séries/The Good Doctor',
        'filters': ['1080p']
    }
]

joblib.dump(tv_shows, 'data/tv_shows.joblib')
