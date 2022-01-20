import os
from imdbProject import returnFromInput, exportCSV


def main():
    file_paths = ['docs/cleaned_imdb_data.csv', 'docs/non_ascii_complete_imdb_data.csv',
                  'docs/non_ascii_part_imdb_data.csv', 'docs/part_imdb_data.csv']
    for filePath in file_paths:
        if os.path.exists(filePath):
            os.remove(filePath)
    exportCSV.export_clean()
    exportCSV.export_non_ascii_complete()
    exportCSV.export_non_ascii_part()
    exportCSV.export_part()
    returnFromInput.user_input()


if __name__ == "__main__":
    main()
