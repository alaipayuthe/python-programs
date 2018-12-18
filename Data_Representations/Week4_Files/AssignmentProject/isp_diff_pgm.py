"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.
"""
# Constant value which indicates if the lines are identical
IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    # Find the length of the two lines
    line1_length = len(line1)
    line2_length = len(line2)
    # Calculate the loop limit
    if line1_length == line2_length:
        counter = range(line1_length)
    elif line1_length < line2_length:
        counter = range(line1_length)
    else:
        counter = range(line2_length)

    if (not line1_length) and (not line2_length):
        diff_index = IDENTICAL
    elif (not line1_length) or (not line2_length):
        diff_index = 0 
    else:
        index = 0
        diff_found = False
        # Iterate through the string to find the index of first difference
        for index in counter:
            if line1[index] != line2[index]:
                diff_found = True
                break
        # Assign index of first difference or IDENTICAL to the return value
        if diff_found is True:
            diff_index = index
        elif line1_length < line2_length or (line2_length < line1_length):
            diff_index = index + 1
        else:
            diff_index = IDENTICAL
    
    return diff_index

#print(str(singleline_diff("Krishna", "krishna")))
#print(str(singleline_diff("Bhanu", "BhAnu")))
#print(str(singleline_diff("Neeharam", "Neehara")))
#print(str(singleline_diff('', 'a')))
#print(str(singleline_diff('', '')))

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """

    # Find the length of the input lines
    line1_length = len(line1)
    line2_length = len(line2)
    # Calculate the maximum possible value of index
    if line1_length < line2_length:
        idx_max = line1_length
    else:
        idx_max = line2_length
    # Validate input index; check if \n or \r is present in input strings
    if idx < 0 or (idx > idx_max):
        return_val = ""
    elif "\n" in line1 or "\r" in line1:
        return_val = ""
    elif "\n" in line2 or "\r" in line2:
        return_val = ""
    else:
        # Otherwise, format the output to human readable format
        diff_string = idx*"=" + "^"
        return_val = line1 + "\n" + diff_string + "\n" + line2 + "\n"
    return return_val

#print(str(singleline_diff_format("Krishna", "krishna", 0)))
#print(str(singleline_diff_format("Bhanu", "BhAnu", 2)))
#print(str(singleline_diff_format("Neeharam", "Neehara", 7)))

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    index = IDENTICAL
    diff_found = False

    if len(lines1) < len(lines2):
        short_len = len(lines1)
    else:
        short_len = len(lines2)
    # Iterate through the list of strings, find the first difference in each line
    for idx in range(short_len):
        index = singleline_diff(lines1[idx], lines2[idx])
        if index != IDENTICAL:
            line_num = idx
            diff_found = True
            break
    # Return tuple of line number and index of first difference;
    # otherwise return tuple of invalid values
    if diff_found:
        return_val = (line_num, index)
    elif len(lines1) < len(lines2):
        return_val = (len(lines1), 0)
    elif len(lines2) < len(lines1):
        return_val = (len(lines2), 0)
    else:
        return_val = (IDENTICAL, IDENTICAL)
    return return_val

#print(multiline_diff(["Krishna", "Bhanu", "Neeharam"], ["krishna", "BhAnu", "Neehara"]))
#print(multiline_diff(["Krishna", "Bhanu", "Neeharam"], ["Krishna", "Bhanu", "Neeharam"]))
#print(multiline_diff(["Krishna", "Bhanu", "Neeharam"], ["Krishna", "Bhanu"]))
#print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list1 = []
    # Open the file to be read
    file_handle = open(filename, "rt")
    # Read the lines to a list stripping off the whitespace characters
    for line in file_handle:
        list1.append(line.rstrip())
    # Close the file
    file_handle.close()
    return list1

#print(get_file_lines("file1.txt"))
#print(get_file_lines("file8.txt"))
#print(get_file_lines("file10.txt"))

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    # Read lines from files to two lists
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    # Pass the lists to multiline_diff() to get the line number and index of difference
    diff = multiline_diff(list1, list2)
    # Format the output string as required and return it
    if diff[0] == IDENTICAL and diff[1] == IDENTICAL:
        output_string = "No differences\n"
    else:
        output_string = "Line " + str(diff[0]) + ":\n"
        if len(list1) < diff[0]:
            line1 = ""
        else:
            if list1 != []:
                line1 = list1[diff[0]]
            else:
                line1 = ""

        if len(list2) < diff[0]:
            line2 = ""
        else:
            if list2 != []:
                line2 = list2[diff[0]]
            else:
                line2 = ""
        output_string = output_string + singleline_diff_format(line1, line2, diff[1])
    return output_string

#print(file_diff_format("file1.txt", "file2.txt"))
#print(file_diff_format("file1.txt", "file4.txt"))
#print(file_diff_format("file4.txt", "file5.txt"))
#print(file_diff_format("file4.txt", "file4.txt"))
#print(file_diff_format("file6.txt", "file7.txt"))
#print(file_diff_format("file8.txt", "file9.txt"))
