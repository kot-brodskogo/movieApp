from abc import ABC, abstractmethod


class IStorage(ABC):
    """ Interface for storing movie data. """

    @abstractmethod
    def list_movies(self):
        """ List all movies stored in the storage. """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster_url, country, imdb_id, notes):
        """ Add a new movie to the storage.

            Args:
                title (str): The title of the movie.
                year (int): The release year of the movie.
                rating (float): The rating of the movie.
                poster_url (str): The URL of the movie's poster.
                country (str): The country of origin for the movie.
                imdb_id (str): The IMDb ID of the movie.
                notes (str): Additional notes about the movie.

            Returns:
                None
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """ Delete a movie from the storage.

            Args:
                title (str): The title of the movie to delete.

            Returns:
                None
        """
        pass

    @abstractmethod
    def update_movie(self, title, notes):
        """ Update the rating of a movie in the storage.

            Args:
                title (str): The title of the movie to update.
                notes (str): The new notes for the movie.

            Returns:
                None
        """
        pass
