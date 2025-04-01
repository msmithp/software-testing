def format_revenue(num): # Format an integer in dollars.
    return "$" + str(num) + ".00"

def format_movie(title, revenue): # Format movie title and its revenue into a string
    return "Title: " + title + ", Revenue: " + format_revenue(revenue)

def get_max(movies): # Return the movie title that has the highest revenue
    movie_revenues = []
    for movie in movies:
        movie_revenues.append(movie['revenue'])
    
    for movie in movies: 
        if movie['revenue'] == max(movie_revenues):
            biggest = movie

    format = format_movie(biggest['title'], biggest['revenue'])
    
    return format

def get_min(movies): # Return the movie title that has the lowest revenue
    movie_revenues = []
    for movie in movies:
        movie_revenues.append(movie['revenue'])

    for movie in movies:
        if movie['revenue'] == min(movie_revenues):
            smallest = movie

    format = format_movie(smallest['title'], smallest['revenue'])
    
    return format

def get_avg(movies): # Return the average of all movie revenues
    total = 0
    for movie in movies:
        total += movie['revenue']
    avg = total/len(movies)
    new_avg = int(rounding(avg))

    avg_cash = format_revenue(new_avg)
    return avg_cash

def rounding(num): # Round a number to the nearest million
    if num%1000000 == 0:
        if num%1000000 >= 500000:
            new_num = num - (num%1000000) + 1000000
        elif num%1000000 < 500000:
            new_num = num - (num%1000000)

    return new_num
