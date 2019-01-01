"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    fieldnames_list = list()
    # Open and read the csv file, return the field names in the file
    with open(filename, "rt") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator,
                                    quotechar=quote, quoting=csv.QUOTE_ALL)
        fieldnames_list.extend(csv_reader.fieldnames)

    return fieldnames_list

#print(read_csv_fieldnames("table1.csv", ',', "'"))
#print(read_csv_fieldnames("table2.csv", ',', "\""))
#print(read_csv_fieldnames("table3.csv", ',', "'"))
#print(read_csv_fieldnames("table4.csv", ',', "'"))
#print(read_csv_fieldnames("table5.csv", ',', "'"))
#print(read_csv_fieldnames("table6.csv", ',', "'"))
#print(read_csv_fieldnames("table7.csv", ',', "'"))

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    list_dict = list()
    # Open and read the csv file, return as list of dictionaries
    with open(filename, "rt") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator,
                                    quotechar=quote, quoting=csv.QUOTE_ALL)
        for row in csv_reader:
            temp_dict = dict()
            for field in csv_reader.fieldnames:
                temp_dict[field] = row[field]
            list_dict.append(temp_dict)
    return list_dict

#print(read_csv_as_list_dict("table1.csv", ',', "'"))
#print(read_csv_as_list_dict("table2.csv", ',', "\""))
#print(read_csv_as_list_dict("table3.csv", ',', "'"))
#print(read_csv_as_list_dict("table4.csv", ',', "'"))
#print(read_csv_as_list_dict("table5.csv", ',', "'"))
#print(read_csv_as_list_dict("table6.csv", ',', "'"))
#print(read_csv_as_list_dict("table7.csv", ',', "'"))

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    temp_nested_dict = dict()
     # Open and read the csv file, return as list of dictionaries
    with open(filename, "rt") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator,
                                    quotechar=quote, quoting=csv.QUOTE_ALL)
        for row in csv_reader:
            temp_dict = dict()
            for field in csv_reader.fieldnames:
                temp_dict[field] = row[field]
            temp_nested_dict[row[keyfield]] = temp_dict
        return temp_nested_dict

#print(read_csv_as_nested_dict("table1.csv", "Field1", ',', "'"))
#print(read_csv_as_nested_dict("table2.csv", "Field 2", ',', "\""))
#print(read_csv_as_nested_dict("table3.csv", "Field 3", ',', "'"))
#print(read_csv_as_nested_dict("table4.csv", "Field 4", ',', "'"))
#print(read_csv_as_nested_dict("table5.csv", "Field 1", ',', "'"))
#print(read_csv_as_nested_dict("table6.csv", "Field 1", ',', "'"))
#print(read_csv_as_nested_dict("table7.csv", "Field 2", ',', "'"))


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    # Open and write list of dictionaries to the mentioned file
    with open(filename, "wt") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=separator,
                                    quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(table)

#field_names = read_csv_fieldnames("table1.csv", ',', "'")
#table = read_csv_as_list_dict("table1.csv", ',', "'")
#write_csv_from_list_dict("copy1.csv", table, field_names, ',', "'")
#print(read_csv_as_list_dict("copy1.csv", ',', "'"))

#field_names = read_csv_fieldnames("table2.csv", ',', "\"")
#table = read_csv_as_list_dict("table2.csv", ',', "\"")
#write_csv_from_list_dict("copy2.csv", table, field_names, ',', "\"")
#print(read_csv_as_list_dict("copy2.csv", ',', "\""))

#field_names = read_csv_fieldnames("table3.csv", ',', "'")
#table = read_csv_as_list_dict("table3.csv", ',', "'")
#write_csv_from_list_dict("copy3.csv", table, field_names, ',', "'")
#print(read_csv_as_list_dict("copy3.csv", ',', "'"))

#field_names = read_csv_fieldnames("table4.csv", ',', "'")
#table = read_csv_as_list_dict("table4.csv", ',', "'")
#write_csv_from_list_dict("copy4.csv", table, field_names, ',', "'")
#print(read_csv_as_list_dict("copy4.csv", ',', "'"))

#field_names = read_csv_fieldnames("table5.csv", ',', "'")
#table = read_csv_as_list_dict("table5.csv", ',', "'")
#write_csv_from_list_dict("copy5.csv", table, field_names, ',', "'")
#print(read_csv_as_list_dict("copy5.csv", ',', "'"))

#field_names = read_csv_fieldnames("table6.csv", ',', "'")
#table = read_csv_as_list_dict("table6.csv", ',', "'")
#write_csv_from_list_dict("copy6.csv", table, field_names, ',', "'")
#print(read_csv_as_list_dict("copy6.csv", ',', "'"))

#field_names = read_csv_fieldnames("table7.csv", ',', "'")
#table = read_csv_as_list_dict("table7.csv", ',', "'")
#write_csv_from_list_dict("copy7.csv", table, field_names, ',', "'")
#print(read_csv_as_list_dict("copy7.csv", ',', "'"))
