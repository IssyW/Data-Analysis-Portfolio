# Connecting to the API
import tmdbsimple as tmdb
import pandas as pd

tmdb.API_KEY = '6c37d50741c7004f344af19bf3a67b10'

def main():
    check_diary()

def check_diary():
    search = tmdb.Search()
    discover = tmdb.Discover()

    # 2.Extract titles and release years of watched films

    # Import watched.csv
    diary_df = pd.read_csv ("diary.csv")
    
    # Extract the titles and release years for each film into a list
    title = diary_df.Name.tolist()
    release_year= diary_df.Year.tolist()

    # Create list of film ids
    Film_id = []

    for i,j in zip(title, release_year):
        response = search.movie(query= i, year=j)
        for value in response['results']:
             # This if statement is to exclude results with inaccurate match 
            if value['title'] == i:  
                Film_id.append(value['id'])
                # Only take first result to avoid redundant
                break

    Film_info = []

    # Create list of film info from ids
    for i in Film_id:
        film = tmdb.Movies(i)
        response = film.info()
        Film_info.append([film.id, film.title, film.spoken_languages, film.production_countries, film.genres, film.runtime, film.release_date])

    
    # Convert to dataframe and export to csv
    film_df = pd.DataFrame(Film_info, columns =['ID', 'title', 'languages', 'prod_country', 'genres', 'runtime', 'releasedate'])
    film_df.head()

    film_df.to_csv('watchedmovie.csv')
    print("Exported movies successfully!")





if __name__ == "__main__":
    main()