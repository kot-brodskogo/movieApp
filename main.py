import argparse
from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    parser = argparse.ArgumentParser(description="Movie App with customizable storage")
    parser.add_argument("file_path", help="Path to the storage file")
    args = parser.parse_args()

    # Determine storage type based on file extension
    if args.file_path.endswith('.json'):
        storage = StorageJson(args.file_path)
    elif args.file_path.endswith('.csv'):
        storage = StorageCsv(args.file_path)
    else:
        print("Unsupported file type. Please provide a JSON or CSV file.")
        return

    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
