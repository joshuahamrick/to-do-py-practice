favorite_movies = []


def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added")


def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
    else:
        print(f"Movie '{movie}' not found")


def display_movies():
    print("Favorite Movies:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    counter = 0
    for movie in favorite_movies:
        counter += 1
    return print(f"There are {counter} movies in your movies list.")

def find_movie(movie):
    for single_movie in favorite_movies:
        if single_movie == movie:
            return print(f"Movie found")
        else:
            return print(f"Cannot locate movie.")

def clear_movies():
    favorite_movies.clear()
    return print("All movies removed.")

add_movie("Movie 0")
add_movie("Movie 1")
add_movie("Movie 2")

display_movies()

remove_movie("Movie 0")

display_movies()

count_movies()

find_movie("Movie 1")

clear_movies()

display_movies()
display_movies()