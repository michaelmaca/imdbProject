# -*- coding: utf-8 -*-
import pandas as pd

pd.options.display.width = 0
pd.options.display.max_rows = 10000
pd.options.display.max_info_columns = 10000
CSVFILE = '../docs/imdb_data.csv'


def read_csv():
    # create dataframe from csv file and remove white space
    df = pd.read_csv(CSVFILE,
                     converters={'title': str.strip})
    df["id"] = df.index + 1
    return df


def drop_na():
    full_df = read_csv()
    # creating a completed df using dropna to remove rows with na values
    no_na_df = full_df.dropna(axis=0, how='any')
    return no_na_df


def na_data():
    # dropping duplicates so we have a df of only rows with missing values
    return pd.concat([read_csv(), drop_na()]).drop_duplicates(keep=False)


def remove_non_ascii(df):
    non_ascii_df = df
    for index, row in df.iterrows():
        # nested function to check for ascii values
        def check_ascii():
            for entity in row:
                for char in str(entity):
                    # check if character is non ascii
                    if ord(char) > 128:
                        # if found drop row by index and return out of loop
                        non_ascii_df.drop(index=index, inplace=True)
                        return
        check_ascii()
    return non_ascii_df


def complete_data():
    return remove_non_ascii(drop_na())


def non_ascii_complete_data():
    return pd.concat([drop_na(), complete_data()]).drop_duplicates(keep=False)


def part_data():
    return remove_non_ascii(na_data())


def non_ascii_part_data():
    return pd.concat([na_data(), part_data()]).drop_duplicates(keep=False)
