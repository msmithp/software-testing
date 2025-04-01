from movie_data import get_movie_info

movies = [
    {
        'title': 'Sunset',
        'release date': 1997,
        'revenue': 80000000,
    },
    {
        'title': 'Lifelock',
        'release date': 2024,
        'revenue': 620000000
    },
    {
        'title': 'Terror',
        'release date': 2013,
        'revenue': 150000000
    },
    {
        'title': 'Meningitis: A Documentary',
        'release date': 2003,
        'revenue': 73057920
    },
    {
        'title': 'The Best Movie Ever Made',
        'release date': 2025,
        'revenue': 98840000
    },
    {
        'title': 'Battlefield Mars',
        'release date': 2000,
        'revenue': 29700000
    }
]

# Write your tests here.
def test_movies():
    assert get_movie_info(movies)

def movie_test(movies):
    print(get_movie_info(movies))

#movie_test(movies)
movie_test(movies)