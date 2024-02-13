import os
import csv
import json


def convert_movie_info():
    field_names = ["movie_id", "imdb_id", "popularity", "budget", "revenue", "original_title", "cast", "homepage",
                   "director", "tagline", "keywords", "overview", "runtime", "genres", "production_companies",
                   "release_date", "vote_count", "vote_average", "release_year", "budget_adj", "revenue_adj"]

    with open("TMDB Reviews Datasets/raw data/tmdb_movies_data.csv") as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=field_names)
        json_text = json.dumps( [ row for row in reader ] )

    json_content = json.loads(json_text)

    elasticsearch_data = []

    with open("TMDB Reviews Datasets/tmdb_movies_data.json", mode="w") as json_file:
        for row in json_content:
            doc = dict()
            doc["_op_type"] = "index"
            doc["_index"] = "movie_info"
            doc["title"] = row["movie_id"]
            doc["doc"] = row

            elasticsearch_data.append(doc)

        json_file.write(json.dumps(elasticsearch_data))


def convert_movie_reviews():
    elasticsearch_data = list()

    folder_path = "TMDB Reviews Datasets/raw data"

    file_names = os.listdir(folder_path)
    for file_name in file_names:
        if file_name.endswith("reviews.json"):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path) as file:
                for row in file:
                    content = json.loads(row)

                    #review = content["content"]
                    #review = review.replace("\r", "")
                    #review = review.replace("\n", "")

                    #print(review)

                    doc = dict()
                    doc["_op_type"] = "index"
                    doc["_index"] = "movie_review"
                    doc["title"] = content["movie_id"]
                    doc["doc"] = content

                    elasticsearch_data.append(doc)

    with open("TMDB Reviews Datasets/tmdb-movies-reviews.json", mode="w") as json_file:
        json_file.write(json.dumps(elasticsearch_data))


def list_file_names():
    file_names = os.listdir("TMDB Reviews Datasets/raw data")
    for file_name in file_names:
        if file_name.endswith("reviews.json"):
            print(file_name)


if __name__ == '__main__':
    # list_file_names()

    convert_movie_info()

    convert_movie_reviews()




