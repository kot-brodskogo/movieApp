from istorage import IStorage
import json
import os


class StorageJson(IStorage):
    """Class for handling movie storage using JSON files."""

    def __init__(self, file_path):
        """
            Initializes the StorageJson instance.

            Args:
                file_path (str): The path to the JSON file used for storage.
            """
        self.__file_path = file_path
        if not os.path.exists(self.__file_path):
            self._create_empty_json_file()
            print(f"Storage file '{self.__file_path}' created successfully.")

    def _create_empty_json_file(self):
        """Create an empty JSON file if it does not exist."""
        with open(self.__file_path, 'w') as f:
            f.write('{}')  # Write an empty JSON object to the file

    def list_movies(self):
        """
            Lists all movies stored in the JSON file.

            Returns:
                dict: A dictionary containing movie titles as keys and movie information as values.
            """
        with open(self.__file_path, 'r') as json_file:
            movies = json.load(json_file)
        return movies

    def add_movie(self, title, year, rating, poster_url, country, imdb_id, notes):
        """
            Adds a new movie to the JSON file.

            Args:
                title (str): The title of the movie.
                year (str): The release year of the movie.
                rating (float): The rating of the movie.
                poster_url (str): The URL of the movie poster.
                country (str): The country of origin of the movie.
                imdb_id (str): The IMDb ID of the movie.
                notes (str): Any additional notes about the movie.
            """
        movies = self.list_movies()
        movies[title] = {"rating": rating, "year": year, "poster_url": poster_url, "country": country,
                         "imdb_id": imdb_id, "notes": notes}
        self._write_movies_to_file(movies)

    def delete_movie(self, title):
        """
            Deletes a movie from the JSON file.

            Args:
                title (str): The title of the movie to delete.
            """
        movies = self.list_movies()
        del movies[title]
        self._write_movies_to_file(movies)

    def update_movie(self, title, notes):
        """
            Updates the notes for a movie in the JSON file.

            Args:
                title (str): The title of the movie to update.
                notes (str): The new notes for the movie.
            """
        movies = self.list_movies()
        if title in movies:
            movies[title]["notes"] = notes
            self._write_movies_to_file(movies)

    def _write_movies_to_file(self, movies):
        """
            Writes the movie data to the JSON file.

            Args:
                 movies (dict): A dictionary containing movie data to be written to the file.
            """
        with open(self.__file_path, 'w') as json_file:
            json.dump(movies, json_file, indent=4)
