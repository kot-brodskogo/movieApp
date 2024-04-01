import matplotlib.pyplot as plt
from fuzzywuzzy import process
from colorama import Fore
from movie_api import MovieAPI
from website_generator import WebsiteGenerator
from statistics import Statistics
from istorage import IStorage


class MovieApp:
    """MovieApp class for managing movie-related operations.

        Attributes:
            WEBSITE_TITLE (str): The title of the generated movie website.
            menu_options (dict): A dictionary mapping menu choices to corresponding functions.
        """
    WEBSITE_TITLE = 'My Movie App'
    menu_options = {
        "0": ("Exit", "movies_exit"),
        "1": ("List movies", "movies_print"),
        "2": ("Add movie", "movies_add"),
        "3": ("Delete movie", "movies_delete"),
        "4": ("Update movie notes", "movies_update"),
        "5": ("Stats", "movies_stats"),
        "6": ("Random movie", "movies_random"),
        "7": ("Search movie", "movies_search"),
        "8": ("Movies sorted by rating", "movies_by_rating"),
        "9": ("Create rating Histogram", "movies_rating_histogram"),
        "10": ("Generate website", "movies_website_generate")
    }

    def __init__(self, storage_instance: IStorage):
        """
            Initializes the MovieApp instance.

            Args:
                storage_instance (IStorage): An instance of the storage interface for movie data storage.
            """
        self.storage = storage_instance

    def menu_print(self):
        """Prints the menu options."""
        print("\n" + Fore.CYAN + "Menu:")

        for key, value in self.menu_options.items():
            print(f"{key}. {value[0]}")

    def run(self):
        """Runs the MovieApp."""
        print(Fore.GREEN + "********** My Movies Database **********")

        while True:
            self.menu_print()
            choice = input("\n" + Fore.GREEN + "Enter choice (0-10): " + Fore.RESET)

            if choice in self.menu_options:
                try:
                    function_name = self.menu_options[choice][1]
                    getattr(self, function_name)()  # Call the instance method with self
                    input(Fore.YELLOW + "Press Enter to continue..." + Fore.RESET)
                except Exception as e:
                    print(Fore.RED + f"An error occurred: {e}")
            else:
                print(Fore.RED + "Invalid choice. Please enter a valid number from the menu.")

    @staticmethod
    def movies_exit():
        """ Function prints a farewell message and then exits the application.
            """
        print("Exiting the movie app. Goodbye!")
        exit()

    def movies_print(self):
        """ Function prints all the movies, along with their rating and year.
            Also prints how many movies there are in the database.
            """
        movies = self.storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            print(f"{len(movies)} movies in total")
            for title, info in movies.items():
                print(f"{title}, Rating: {info['rating']}, Year: {info['year']}")

    def movies_add(self):
        """ Function asks user to enter movie name, rating and a year,
            then adds them to movies database
            """
        movies = self.storage.list_movies()
        title = input("Please enter a movie name: ")

        try:
            # Check if the inputted title partially matches any existing movie names
            existing_movies = [movie for movie in movies if title.lower() in movie.lower()]

            if existing_movies:
                print(
                    Fore.RED + f"Movie {title} or similar already exists!"
                               f"Existing matches: {', '.join(existing_movies)}. "
                               f"If you want to add another movie, try enter it's full title.\n")
                return

            # Fetch movie information from OMDb
            movie_info = MovieAPI.fetch_movie_info(title)

            if movie_info['Response'] == 'True':
                title = movie_info.get('Title', '')
                year = movie_info.get('Year', '')
                rating = float(movie_info.get('imdbRating', 0.0))
                poster_url = movie_info.get('Poster', '')
                country = movie_info.get('Country', '')
                if ',' in country:
                    country = country.split(', ')[0]
                imdb_id = movie_info.get('imdbID', '')

                self.storage.add_movie(title, year, rating, poster_url, country, imdb_id, notes='')
                print(f"Movie {title} successfully added")
            else:
                print(Fore.RED + f"Movie {title} not found on OMDb.\n")
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}\n")

    def movies_delete(self):
        """ Function asks user which movie to delete, and deletes it.
            If the movie does not exist, prints an error message
            """
        movies = self.storage.list_movies()
        title = input("Please enter a movie name: ")
        movie = movies.get(title)

        if movie:
            self.storage.delete_movie(title)
            print(f"Movie '{title}' has been deleted from the database.")
        else:
            print(Fore.RED + "Error. No such movie name in a database")

    def movies_update(self):
        """ Function asks user which movie to update and if it exists, asks user for notes
            If the movie does not exist prints an error message.
            """
        # Get the data from the JSON file
        movies = self.storage.list_movies()
        title = input("Enter movie name: ")
        if title not in movies:
            print(Fore.RED + f"Error: Movie '{title}' doesn't exist in database.\n")
            return

        notes = input(f"Enter movie notes for '{title}': ")
        self.storage.update_movie(title, notes)
        print(f"Notes added for movie '{title}'.\n")

    def movies_stats(self):
        """ Prints statistics about the movies in the database:
            - Average rating
            - Median rating
            - Best movie(s) by rating
            - Worst movie(s) by rating
            """
        movies = self.storage.list_movies()
        if not movies:
            print("No movies found.")
            return

        average_rating = Statistics.calculate_average_rating(movies)
        median_rating = Statistics.calculate_median_rating(movies)
        best_rating, best_movies = Statistics.find_best_movies(movies)
        worst_rating, worst_movies = Statistics.find_worst_movies(movies)

        print(f"Average rating: {average_rating}")
        print(f"Median rating: {median_rating}")
        print(f"Best movie(s) by rating ({best_rating}): {', '.join(best_movies)}")
        print(f"Worst movie(s) by rating ({worst_rating}): {', '.join(worst_movies)}")

    def movies_random(self):
        """ Picks a random movie from the movies dictionary and prints its name and rating.
            """
        import random
        # Get the data from the JSON file
        movies = self.storage.list_movies()
        random_movie_name = random.choice(list(movies.keys()))

        # Access the rating and year using the selected movie name
        movie_info = movies[random_movie_name]
        rating = movie_info['rating']
        year = movie_info['year']

        print(f"Random movie: {random_movie_name}, Rating: {rating}, Year: {year}")

    @staticmethod
    def get_original_movie_name(movies, term_lower):
        """ Get the original movie name from the dictionary based on its lowercase version. """
        return next(name for name in movies.keys() if name.lower() == term_lower)

    def movies_search(self):
        """
            Searches for movies with fuzzy matching and suggests similar movie names.
            """
        movies = self.storage.list_movies()
        term = input("Enter the title of the movie to search for: ")
        term_lower = term.lower()

        # Convert movie names to lowercase for case-insensitive comparison
        movie_names_lower = [name.lower() for name in movies.keys()]

        # Using fuzzywuzzy process.extract function to get similar matches
        similar_matches = process.extract(term_lower, movie_names_lower, limit=3)

        if term_lower in movie_names_lower:
            original_movie_name = self.get_original_movie_name(movies, term_lower)
            print(f"Movie '{original_movie_name}' found with exact match.")
        elif similar_matches:
            print(f"The movie '{term}' does not exist. Did you mean:")
            for similar_movie, score in similar_matches:
                original_movie_name = self.get_original_movie_name(movies, similar_movie)
                print(f"{original_movie_name}")
        else:
            print(f"No results found for '{term}'.")

    def movies_by_rating(self):
        """Prints movies sorted by their ratings in descending order.
            """
        # Get the data from the JSON file
        movies = self.storage.list_movies()
        print("Movies sorted by rating:")
        for title, info in sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True):
            rating = info['rating']
            year = info['year']
            print(f"{title} (Rating: {rating}, Year: {year})")

    def movies_rating_histogram(self):
        """Creates a histogram of the ratings of the movies and saves the plot to a file."""
        # Get the data from the JSON file
        movies = self.storage.list_movies()
        ratings = [movie['rating'] for movie in movies.values()]

        plt.hist(ratings, bins=10, alpha=0.5, edgecolor='black')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.title('Rating Histogram')
        plt.savefig('rating_histogram.png')
        print('Histogram saved to rating_histogram.png')

    def movies_website_generate(self):
        """ Generates a movies website by replacing placeholders in the HTML template """
        # Get the data from the JSON file
        movies = self.storage.list_movies()

        WebsiteGenerator.generate_website_content(
            movies,
            '_static/index_template.html',
            '_static/index.html',
            self.WEBSITE_TITLE
        )
