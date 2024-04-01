class Statistics:
    @staticmethod
    def calculate_average_rating(movies):
        """Calculates and returns the average rating of movies.

        Args:
            movies (dict): Dictionary containing movie names and ratings.

        Returns:
            float: The average rating of movies."""
        ratings = [movie['rating'] for movie in movies.values()]
        return sum(ratings) / len(ratings) if ratings else 0.0

    @staticmethod
    def calculate_median_rating(movies):
        """Calculates and returns the median rating of movies.

        Args:
            movies (dict): Dictionary containing movie names and ratings.

        Returns:
            float: The median rating of movies."""
        ratings = [info['rating'] for info in movies.values()]
        ratings.sort()
        n_movies = len(ratings)
        if n_movies % 2 == 0:
            median_rating = (ratings[n_movies // 2 - 1] + ratings[n_movies // 2]) / 2
        else:
            median_rating = ratings[n_movies // 2]
        return median_rating

    @staticmethod
    def find_best_movies(movies):
        """Finds and returns the best-rated movies along with their rating.

        Args:
            movies (dict): Dictionary containing movie names and ratings.

        Returns:
            tuple: A tuple containing the best rating and a list of best-rated movie names."""
        best_rating = max(movie['rating'] for movie in movies.values())
        best_movies = [title for title, info in movies.items() if info['rating'] == best_rating]
        return best_rating, best_movies

    @staticmethod
    def find_worst_movies(movies):
        """Finds and returns the worst-rated movies along with their rating.

        Args:
            movies (dict): Dictionary containing movie names and ratings.

        Returns:
            tuple: A tuple containing the worst rating and a list of worst-rated movie names."""
        worst_rating = min(movie['rating'] for movie in movies.values())
        worst_movies = [title for title, info in movies.items() if info['rating'] == worst_rating]
        return worst_rating, worst_movies
