from .context import extractCSV

# rows in full data
print(len(extractCSV.read_csv().index))
# rows in complete data
print(len(extractCSV.complete_data().index))
# rows in partial data
print(len(extractCSV.part_data().index))
# rows in partial data with drop na (should be 0)
print(len(extractCSV.part_data().dropna().index))
# rows in the sum of complete data and partial data
print(len(extractCSV.complete_data().index) + len(extractCSV.part_data().index))
