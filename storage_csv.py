from istorage import IStorage
import csv


class StorageCsv(IStorage):
    """Class for handling movie storage using CSV files."""

    def __init__(self, file_path):
        """
            Initializes the StorageCsv instance.

            Args:
                file_path (str): The path to the CSV file.
            """
        self.__file_path = file_path

    def list_movies(self):
        """
            Reads movie data from the CSV file and returns it as a dictionary.

            Returns:
                dict: A dictionary containing movie titles as keys and movie information as values.
            """
        movies = {}
        with open(self.__file_path, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                movies[row['title']] = {
                    'rating': float(row['rating']),
                    'year': int(row['year']),
                    'poster_url': row['poster_url'],
                    'country': row['country'],
                    'imdb_id': row['imdb_id'],
                    'notes': row['notes']
                }
        return movies

    def add_movie(self, title, year, rating, poster_url, country, imdb_id, notes):
        """
            Reads movie data from the CSV file and returns it as a dictionary.

            Returns:
                dict: A dictionary containing movie titles as keys and movie information as values.
            """
        movie_data = {
            'title': title,
            'rating': rating,
            'year': year,
            'poster_url': poster_url,
            'country': country,
            'imdb_id': imdb_id,
            'notes': notes
        }
        with open(self.__file_path, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=movie_data.keys())
            if csv_file.tell() == 0:  # Check if file is empty
                writer.writeheader()
            writer.writerow(movie_data)

    def delete_movie(self, title):
        """
            Deletes a movie entry from the CSV file.

            Args:
                title (str): The title of the movie to delete.
            """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._write_movies_to_file(movies)

    def update_movie(self, title, notes):
        """
            Updates the notes for a specific movie in the CSV file.

            Args:
                title (str): The title of the movie to update.
                notes (str): The new notes or comments for the movie.
            """
        movies = self.list_movies()
        if title in movies:
            movies[title]['notes'] = notes
            self._write_movies_to_file(movies)

    def _write_movies_to_file(self, movies):
        """
            Writes movie data to the CSV file.

            Args:
                movies (dict): A dictionary containing movie titles as keys and movie information as values.
            """
        with open(self.__file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['title', 'rating', 'year',
                                                          'poster_url', 'country', 'imdb_id', 'notes'])
            writer.writeheader()
            for movie_title, movie_data in movies.items():
                writer.writerow({
                    'title': movie_title,
                    'rating': movie_data['rating'],
                    'year': movie_data['year'],
                    'poster_url': movie_data['poster_url'],
                    'country': movie_data['country'],
                    'imdb_id': movie_data['imdb_id'],
                    'notes': movie_data['notes']
                })
