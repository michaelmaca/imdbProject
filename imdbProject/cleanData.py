from imdbProject import extractSortCSV


def change_data_type():
    df = extractSortCSV.complete_data()
    df = df.astype({'year': 'int64'})
    df = df.astype({'duration': 'int64'})
    df = df.astype({'budget': 'int64'})
    df = df.astype({'gross': 'int64'})
    # df['year'] = pd.to_datetime(df['year'], format='%Y')
    return df


def genre_to_list():
    df = change_data_type()
    for index, row in df.iterrows():
        genres = row.genres.split('|')
        df.at[index, 'genres'] = genres
    return df
