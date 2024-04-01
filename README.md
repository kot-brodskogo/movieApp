# Movie App 🎬

## Description

The Movie App is a simple command-line application that allows users to manage a collection of movies. Users can add, delete, update, and list movies, as well as perform various operations such as sorting by rating, generating statistics, and creating a movie website.

Movie App uses OMDB API to fetch additional data about movies 🌐.

## Table of Contents

- [Installation](#installation)
- [API Usage](#api-usage)
- [Usage](#usage)
- [Future Update](#future-update)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Installation

To use the Movie App, follow these steps:

1. Clone the repository to your local machine: 
```
git clone https://github.com/your-username/movie-app.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python main.py data.json
```

Replace `data.json` with the path to your JSON storage file. If you're using a CSV file, replace it accordingly.

## API Usage

Movie App uses the OMDB API to fetch additional data about movies. To use this feature, you'll need to obtain an API key from OMDB and set it up in your environment or directly in the code. Refer to the [OMDB API documentation](https://www.omdbapi.com) for more information on how to get started.

## Usage

Once the Movie App is running, you can perform the following actions:

- **List movies:** View the list of movies in the collection.
- **Add movie:** Add a new movie to the collection.
- **Delete movie:** Remove a movie from the collection.
- **Update movie notes:** Update the notes for a specific movie.
- **Stats:** View statistics such as average rating, median rating, best and worst movies.
- **Random movie:** Get a random movie recommendation from the collection.
- **Search movie:** Search for a movie by title.
- **Movies sorted by rating:** View the movies sorted by rating.
- **Create rating histogram:** Generate a histogram of movie ratings.
- **Generate website:** Generate a website with movie data.

## Future update
* Adding unit testing 🛠️
* and more...

## Contributing

Contributions to the Movie App are welcome! If you'd like to contribute, please follow these guidelines:

- Fork the repository and create a new branch.
- Make your changes and ensure the code passes all tests.
- Submit a pull request detailing your changes and any related issues.

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out to the project maintainers:

- Tim Brodsky (tetbetwork@gmail.com)

## Acknowledgements

The Movie App makes use of the following third-party libraries:

- [PyCountry](https://pypi.org/project/pycountry/): For retrieving country information.
- [Colorama](https://pypi.org/project/colorama/): For adding color to the command-line interface.
