def get_movie_info(movies):
    clean_movies = clean_data(movies)
    avg = get_avg(clean_movies)
    return

def clean_data(movies):
    movie_revenues = []
    for movie in movies:
        movie_revenues.append(movie['revenue'])
    
    new_movies = movies
    
    return new_movies

def get_avg(movies):
    total = 0
    for movie in movies:
        total += movie['revenue']
    avg = total/len(movies)
    new_avg = rounding(avg)
    return new_avg

def rounding(num):
    if num%1000000 != 0:
        if num%1000000 >= 500000:
            new_num = num - (num%1000000) + 1000000
        elif num%1000000 <= 500000:
            new_num = num - (num%1000000)

    return new_num
