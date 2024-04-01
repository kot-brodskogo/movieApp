import pycountry


class WebsiteGenerator:
    IMDB_URL = 'https://www.imdb.com/title/'

    @staticmethod
    def __serialize_movie(title, movie_info):
        """ Serializes a single movie info into HTML """
        # Extract fields from movie_info
        year = movie_info.get('year')
        rating = float(movie_info.get('rating'))
        poster_url = movie_info.get('poster_url')
        country = movie_info.get('country')
        imdb_id = movie_info.get('imdb_id')
        notes = movie_info.get('notes')

        # Generate output
        output = ''
        output += '<li>\n'
        output += '    <div class="movie">\n'
        output += f'        <a href="{WebsiteGenerator.IMDB_URL}{imdb_id}" target="_blank">\n'
        output += f'            <img class="movie-poster" src="{poster_url}" {"title=" + repr(notes) if notes else ""}>\n'
        output += f'        </a>\n'
        output += f'        <img class="movie-country-flag" title="{country}" ' \
                  f'src="https://flagsapi.com/{WebsiteGenerator.__get_alpha2_code(country)}/shiny/24.png">\n'
        output += f'        <div class="movie-title">{title}</div>\n'
        output += f'        <div class="movie-year">{year}</div>\n'
        output += f'        <div class="movie-rating" title="{rating}">{WebsiteGenerator.__generate_star_icon(rating)}</div>\n'
        output += '    </div>\n'
        output += '</li>'

        return output

    @staticmethod
    def __get_alpha2_code(country_name):
        """ Get two-letter code for a given country """
        try:
            country = pycountry.countries.get(name=country_name)
            if country:
                return country.alpha_2
            else:
                print(f"Country '{country_name}' not found in the pycountry database.")
        except LookupError as e:
            print(f"Error: {e}")

    @staticmethod
    def __generate_star_icon(rating):
        """ Generates a star icon SVG based on the rating """
        num_stars = 1  # Default to 1 star

        if rating >= 9:
            num_stars = 5
        elif rating >= 7:
            num_stars = 4
        elif rating >= 4.6:
            num_stars = 3
        elif rating >= 2.3:
            num_stars = 2

        star_icon = ''

        for star in range(num_stars):
            star_icon += f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" ' \
                         f'fill="currentColor" class="bi bi-star-fill" viewBox="0 0 24 24">'
            star_icon += '<path d="M12 17.27l4.15 2.51c.76.46 1.69-.22 1.49-1.08l-1.1-4.72 ' \
                         '3.67-3.18c.67-.58.31-1.68-.57-1.75l-4.83-.41-1.89-4.46c-' \
                         '.34-.81-1.5-.81-1.84 0L9.19 8.63l-4.83.41c-.88.07-1.24 1.17-.57 ' \
                         '1.75l3.67 3.18-1.1 4.72c-.2.86.73 1.54 1.49 1.08l4.15-2.5z"/>'
            star_icon += '</svg>'

        return star_icon

    @staticmethod
    def __generate_movies_info(movies):
        """ Generates HTML list items with movies data """
        output = ""
        for title, movie_info in movies.items():
            output += WebsiteGenerator.__serialize_movie(title, movie_info)

        return output

    @staticmethod
    def generate_website_content(movies, template_file_path, output_file_path, website_title):
        """ Generates a movies website by replacing placeholders in the HTML template """
        # Generate a string with movies' data
        movies_info_string = WebsiteGenerator.__generate_movies_info(movies)

        # Read the content of the template file
        with open(template_file_path, 'r') as template_file:
            template_content = template_file.read()

        # Replace __TEMPLATE_MOVIE_GRID__ with the generated string
        new_content = template_content.replace('__TEMPLATE_MOVIE_GRID__', movies_info_string)
        # Replace __TEMPLATE_TITLE__ with my title
        new_content = new_content.replace('__TEMPLATE_TITLE__', website_title)

        # Write the new HTML content to a new file, animals.html
        with open(output_file_path, 'w') as output_file:
            output_file.write(new_content)

        print("Website was generated successfully.")
