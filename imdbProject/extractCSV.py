import pandas as pd

pd.options.display.width = 0
pd.options.display.max_rows = 10000
pd.options.display.max_info_columns = 10000


def read_csv():
    # create dataframe from csv file
    df = pd.read_csv('../docs/imdb_data.csv')
    return df


def complete_data():
    full_df = read_csv()
    # creating a completed df using dropna to remove rows with na values
    complete_df = full_df.dropna(axis=0, how='any')
    return complete_df


def part_data():
    full_df = read_csv()
    complete_df = complete_data()
    # concatenating the two dfs and dropping duplicates so we have a df with with rows with missing values
    part_df = pd.concat([full_df, complete_df]).drop_duplicates(keep=False)
    return part_df
