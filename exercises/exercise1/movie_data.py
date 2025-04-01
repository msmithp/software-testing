def get_max(movies): # Return the movie title that has the highest revenue
    movie_revenues = []
    for movie in movies:
        movie_revenues.append(movie['revenue'])
    
    for movie in movies: 
        if movie['revenue'] == max(movie_revenues):
            biggest = movie
    
    return biggest['title']

def get_min(movies): # Return the movie title that has the lowest revenue
    movie_revenues = []
    for movie in movies:
        movie_revenues.append(movie['revenue'])

    for movie in movies:
        if movie['revenue'] == min(movie_revenues):
            smallest = movie

    return smallest['title']

def get_avg(movies): # Return the average of all movie revenues
    total = 0
    for movie in movies:
        total += movie['revenue']
    avg = total/len(movies)
    new_avg = rounding(avg)
    return int(new_avg)

def rounding(num): # Round a number to the nearest million
    if num%1000000 == 0:
        if num%1000000 >= 500000:
            new_num = num - (num%1000000) + 1000000
        elif num%1000000 < 500000:
            new_num = num - (num%1000000)

    return new_num
