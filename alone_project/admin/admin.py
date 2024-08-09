from datetime import datetime

from file_manager import movies_manager


class MoviesManager:
    def __init__(self, id, movie_name, location, price, total_ticket, date):
        self.id = id
        self.movie_name = movie_name
        self.location = location
        self.price = price
        self.total_ticket = total_ticket
        self.date = date


def add_movie():
    id = 1
    try:
        for movie in movies_manager.read():
            if movie['id']:
                id += 1
        movie_name = input("Enter movie name: ").capitalize().strip()
        location = input("Enter movie location: ").capitalize().strip()
        price = float(input("Enter movie price: "))
        total_ticket = int(input("Enter total number of tickets: "))
        deta = datetime.now().strftime("%Y.%m.%d %H.%M")
        movie = MoviesManager(id, movie_name, location, price, total_ticket, deta)
        movies_manager.add_data(movie.__dict__)
        print("Movie added successfully")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def view_movies():
    try:
        movies = movies_manager.read()
        if not movies:
            print("No movies found.")
            return False
        print("ID\tMovie Name\t\tLocation\t\tPrice\t\tDate")
        for movie in movies:
            print(f"{movie['id']}\t{movie['movie_name']}\t\t{movie['location']}\t{movie['price']}\t{movie['date']}")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def edit_movie():
    try:
        movie_id = int(input("Enter movie ID to edit: "))
        movies = movies_manager.read()
        movie_to_edit = None
        for movie in movies:
            if movie['id'] == movie_id:
                movie_to_edit = movie
                break
        if not movie_to_edit:
            print("Movie not found.")
            return False
        movie_name = input("Enter new movie name (leave blank to keep the same): ")
        if movie_name:
            movie_to_edit['movie_name'] = movie_name
        location = input("Enter new movie location (leave blank to keep the same): ")
        if location:
            movie_to_edit['location'] = location
        price = input("Enter new movie price (leave blank to keep the same): ")
        if price:
            movie_to_edit['price'] = float(price)
        movies_manager.write(movie_to_edit)
        print("Movie edited successfully")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def delete_movie():
    try:
        movie_id = int(input("Enter movie ID to delete: "))
        movies = movies_manager.read()
        movie_to_delete = None
        for movie in movies:
            if movie['id'] == movie_id:
                movie_to_delete = movie
                break
        if not movie_to_delete:
            print("Movie not found.")
            return False
        movies.remove(movie_to_delete)
        movies_manager.write(movies)
        print("Movie deleted successfully")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
