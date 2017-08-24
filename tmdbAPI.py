import tmdbsimple as tmdb
tmdb.API_KEY = '04db55e997b03c28163ee7578127e4f4'


def findmovie(movieName, year):
    search = tmdb.Search()
    s = search.movie(query=movieName, year=year)
    return search.results[1]['id']



def findposter(movieName, year):
    id = findmovie(movieName, year)
    movie = tmdb.Movies(id)
    return movie.images()

