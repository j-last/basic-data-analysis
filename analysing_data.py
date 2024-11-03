def freq_genres(dataset, genre_column, header_row=True):
    """Creates a frequency table (dict) of how many times
        different genres appear in the dataset.
        """
    if header_row: dataset = dataset[1:]

    freq_table = {}

    for row in dataset:
        genre = row[genre_column]

        if freq_table.get(genre) is None:
            freq_table[genre] = 1
        else:
            freq_table[genre] += 1

    for genre in freq_table:
        freq_table[genre] /= len(dataset)  # converts numbers to percentages

    return freq_table


def rank_frequencies(freq_table):
    """Ranks the frequencies in a frequency table from high to low
        and prints them out as percentages.
    """
    mylist = []
    for genre, frequency in freq_table.items():
        mylist.append((frequency, genre))
    
    mylist.sort(reverse=True)

    for frequency, genre in mylist:
        print(f"{genre} - {round(frequency * 100, 1)}%")
    print("\n")


def freq_popularity(dataset, genre_column, installs_column, header_row=True):
    """Creates a frequency table based on how many users use each 
        genre of app.
    """
    if header_row: dataset = dataset[1:]

    total_installs = 0
    freq_table = {}

    for row in dataset:
        genre = row[genre_column]
        installs = int(row[installs_column])

        total_installs += installs

        if freq_table.get(genre) is None:
            freq_table[genre] = installs
        else:
            freq_table[genre] += installs

    for genre in freq_table:
        freq_table[genre] /= total_installs  # converts numbers to percentages

    return freq_table

