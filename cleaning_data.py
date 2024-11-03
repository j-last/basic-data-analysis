def remove_faulty_data(dataset, ID_column):
    """Removes duplicate data or 
    data containing the wrong number of columns.
    """
    # list of app names in order to detect duplicates
    unique_IDs = []
    # list of the indexes to be deleted
    faulty_indexes = []

    for row_index, row in enumerate(dataset):
        id = row[ID_column]
        if id in unique_IDs:  # duplicate data
            faulty_indexes.append(row_index)
            print(row_index)
            print(unique_IDs.index(id))
        elif len(row) != 16:  # incorrect length data
            faulty_indexes.append(row_index)
        else:
            unique_IDs.append(id)

    for index in reversed(faulty_indexes):
        del dataset[index]  # delete faulty data

    return dataset


def remove_unwanted_data(dataset:list, name_column, price_column, header_row=True):
    """Removes apps that aren't free to install or aren't english."""
    if header_row: 
        header_row = dataset[0]
        dataset = dataset[1:]
    unwanted_idexes = []
    for row_index, row in enumerate(dataset):
        price = float(row[price_column])
        name = row[name_column]
        if price > 0:
            unwanted_idexes.append(row_index)
            continue
        non_english_count = 0
        for character in name:
            if ord(character) > 127:
                non_english_count += 1
            if non_english_count >= 3:
                unwanted_idexes.append(row_index)
                break

    for index in reversed(unwanted_idexes):
        del dataset[index]
    
    if header_row:
        dataset.insert(0, header_row)
    
    return dataset


def clean_data(dataset, ID_column, name_column, price_column):
    """Removes all faulty or unwanted data."""
    dataset = remove_faulty_data(dataset, ID_column)
    dataset = remove_unwanted_data(dataset, name_column, price_column)
    return dataset