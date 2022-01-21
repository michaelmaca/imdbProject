import pandas as pd
from operator import gt, lt, ge, le, eq

CSVFILE = 'docs/cleaned_imdb_data.csv'
pd.options.display.width = 0
pd.options.display.max_rows = 10000
pd.options.display.max_info_columns = 10000


def read_clean_data():
    df = pd.read_csv(CSVFILE)
    return df


def user_input():
    print("\nChoose an entity to query by entering the associated number")
    user_in = input("Title: 1    Score: 2    Year: 3    Genre: 4\n"
                    "Input: ")
    query_selector(user_in)
    while True:
        user_in = input("\nWould you like to make another query? Y/N\n"
                        "Input: ")
        match user_in.lower():
            case 'y':
                return user_input()
            case 'yes':
                return user_input()
            case 'n':
                return
            case 'no':
                return
            case _:
                continue


def query_selector(user_in):
    match user_in:
        case '1':
            return title_query()
        case '2':
            return score_query()
        case '3':
            return year_query()
        case '4':
            return genres_query()
        case _:
            print("Lets try that again")
            return user_input()


def title_query():
    df = read_clean_data()
    query_df = df
    query = input("\nEnter the film title you would like to search: ")
    print("Searching...\n")
    for index, row in df.iterrows():
        if query.lower() not in row.title.lower():
            query_df.drop(index=index, inplace=True)
    if query_df.empty:
        print("Whoops, looks like that wasn't a valid title.\n")
        return title_query()
    return print(query_df)


def score_query():
    df = read_clean_data()
    query_df = df
    op_dict = {">": gt, "<": lt, "<=": le, ">=": ge, "==": eq}
    query = input("\nEnter the score you would like to search: ")
    if query.isnumeric():
        oper = input(f"Would you like to find films with a score greater than (>/>=),"
                     f" less than (</<=) or equal to (==) {query}?: ")
        comp = op_dict[oper]
        print("Searching...\n")
        for index, row in df.iterrows():
            if not comp(row.score, float(query)):
                query_df.drop(index=index, inplace=True)
        if query_df.empty:
            print("Whoops, looks like that wasn't a valid score.\n")
            return genres_query()
        return print(query_df)
    print("\nWhoops, looks like that wasn't a valid score.\n")
    return year_query()


def year_query():
    df = read_clean_data()
    query_df = df
    op_dict = {">": gt, "<": lt, "<=": le, ">=": ge, "==": eq}
    query = input("\nEnter the year you would like to search: ")
    if query.isnumeric():
        oper = input(f"Would you like to find films with a year greater than (>/>=),"
                     f" less than (</<=) or equal to (==) {query}?: ")
        comp = op_dict[oper]
        print("Searching...\n")
        for index, row in df.iterrows():
            if not comp(row.year, int(query)):
                query_df.drop(index=index, inplace=True)
        if query_df.empty:
            print("\nWhoops, looks like that wasn't a valid year.\n")
            return year_query()
        return print(query_df)
    print("\nWhoops, looks like that wasn't a valid year.\n")
    return year_query()


# find a way to make genre list lowercase
# if query.lower() not in list(map(lambda x: x.lower(), row.genres)):
# query multiple genres
def genres_query():
    df = read_clean_data()
    query_df = df
    query = input("\nEnter a genre you would like to search: ")
    print("Searching...\n")
    for index, row in df.iterrows():
        if query not in row.genres:
            query_df.drop(index=index, inplace=True)
    if query_df.empty:
        print("Whoops, looks like that wasn't a valid genre.\n"
              "(Tip: check spelling and capitalise the first letter)")
        return genres_query()
    return print(query_df)

