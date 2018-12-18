"""
Week 4 practice project for Python Data Representation
Update syntax for print in CodeSkulptor Docs
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""

# HTML tags that bounds example code
PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"


def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated
    """
    line_mod = line
    # Check if string is not empty
    if line_mod:
        # Strip left white space using built-in string method lstrip()
        #line_mod = line_mod.lstrip(" ")
        # If line is print statement,  use the format() method to add insert parentheses
        if "print " in line_mod:
            line_mod = line_mod.replace("print ", "print(", 1)
            if "# " in line_mod:
                # Handle white space/comments after print statememt
                hash_index = line_mod.find("#")
                line_mod = line_mod[:hash_index] + ")" + line_mod[hash_index:]
            else:
                line_mod = line_mod + ")"

    return line_mod

# Some simple tests
print(update_line(""))
print(update_line("foobar()"))  
print(update_line("print 1 + 1"))      
print(update_line("    print 2, 3, 4"))
print(update_line("    print 2, 3, 4 # Print 2, 3, 4"))
# Expect output
##
##foobar()
##print(1 + 1)
##    print(2, 3, 4)


def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.  
    Returns string corresponding to updated <pre> block with each line
    updated via process_line()
    """
    
    updated_block = ""
    if pre_block:
        lines = pre_block.splitlines()
        length = len(lines)
        iterator = 0
        for line in lines:
            if iterator == 0: 
                updated_block = update_line(line)
                iterator = iterator + 1
            else:
                updated_block = updated_block + "\n" + update_line(line)
                iterator = iterator + 1

    return updated_block

# Some simple tests
print(update_pre_block(""))
print(update_pre_block("foobar()"))
print(update_pre_block("if foo():\n    bar()"))
print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))

# Expected output
##
##foobar()
##if foo():
##    bar()
##print()
##print(1+1)
##print(2, 3, 4)
##    print(a + b)
##    print(23 * 34)
##        print(1234)

def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Process the <pre> blocks in the loaded text to update print syntax
    Write the update text to the file specified by the string output_file_name
    """
    
    # open file and read text in file as a string
    if input_file_name:
        input_file = open(input_file_name, "rt")
        pre_block = ""
        is_pre_block = False
        # split text in <pre> blocks and update using update_pre_block()
        for line in input_file:
            if "<pre>" in line:
                pre_block_start = True
                is_pre_block = True
            else:
                if pre_block_start:
                    if "<\pre>" in line:
                        last_newline = pre_block.rindex("\n")
                        pre_block[last_newline - 1] = ""
                        pre_block_start = False
                    else:
                        pre_block = line + "\n"

            # Write the answer in the specified output file
            if is_pre_block == True && (pre_block_start == False):
                input_file.close()
                output_file = open(output_file_name, "wt")
                output_file.write(update_pre_block(pre_block))

# A couple of test files
update_file("table.html", "table_updated.html")
update_file("docs.html", "docs_updated.html")

# Import some code to check whether the computed files are correct
##import examples3_file_diff as file_diff
##file_diff.compare_files("table_updated.html", "table_updated_solution.html")
##file_diff.compare_files("docs_updated.html", "docs_updated_solution.html")

# Expected output
##table_updated.html and table_updated_solution.html are the same
##docs_updated.html and docs_updated_solution.html are the same

