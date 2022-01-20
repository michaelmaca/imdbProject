import extractSortCSV
import cleanData


def export_clean():
    df = cleanData.genre_to_list()
    df.to_csv('../docs/cleaned_imdb_data.csv', index=False)
    return


def export_non_ascii_complete():
    df = extractSortCSV.non_ascii_complete_data()
    df.to_csv('../docs/non_ascii_complete_imdb_data.csv', index=False)
    return


def export_non_ascii_part():
    df = extractSortCSV.non_ascii_part_data()
    df.to_csv('../docs/non_ascii_part_imdb_data.csv', index=False)
    return


def export_part():
    df = extractSortCSV.part_data()
    df.to_csv('../docs/part_imdb_data.csv', index=False)
    return


# export_clean()
# export_non_ascii_complete()
# export_non_ascii_part()
# export_part()
