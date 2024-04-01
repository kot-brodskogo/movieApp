import argparse
import os
from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    parser = argparse.ArgumentParser(description="Movie App with customizable storage")
    parser.add_argument("file_path", help="Path to the storage file")
    args = parser.parse_args()

    # Determine storage type based on file extension
    if args.file_path.endswith('.json'):
        if not os.path.exists(args.file_path):
            # If the file doesn't exist, create it
            with open(args.file_path, 'w') as f:
                f.write('{}')  # Write an empty JSON object to the file
            print(f"Storage file '{args.file_path}' created successfully.")
        storage = StorageJson(args.file_path)
    elif args.file_path.endswith('.csv'):
        if not os.path.exists(args.file_path):
            # If the file doesn't exist, create it
            with open(args.file_path, 'w') as f:
                f.write('title,rating,year,country,poster_url,imdb_id,notes\n')  # Write the CSV header
            print(f"Storage file '{args.file_path}' created successfully.")
        storage = StorageCsv(args.file_path)
    else:
        print("Unsupported file type. Please provide a JSON or CSV file.")
        return

    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
