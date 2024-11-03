from cleaning_data import clean_data
from analysing_data import freq_genres, freq_popularity, rank_frequencies


def display_data(dataset, start, end):
    print(f"COLUMNS = {len(dataset[0])}, ROWS = {len(dataset)}")

    data_slice = dataset[start:end]

    for row in data_slice:
        for item in row:
            print(item, end=" | ")
        print("\n")


# reading app data from file
app_data = open("AppleStore.csv", "r", encoding="utf-8")
# For whatever reason the lines of the csv file are not sub-lists.
# So, need convert them from strings to lists.
app_data = [row.split(",") for row in app_data]

display_data(app_data, 0, 1)  # prints column headings

app_data = clean_data(app_data, 0, 1, 4)

genre_frequency_table = freq_genres(app_data, 11)
print("GENRE AVAILABILITY: ")
rank_frequencies(genre_frequency_table)

# Note that the dataset doesn't have number of installs,
# so I'm using number of reviews as a judge of popularity.
popularity_frequency_table = freq_popularity(app_data, 11, 5)
print("POPULARITY: ")
rank_frequencies(popularity_frequency_table)
