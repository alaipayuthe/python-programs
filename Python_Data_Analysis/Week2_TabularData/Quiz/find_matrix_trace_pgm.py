NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
for row in my_matrix:
    print(row)

# find the trace of the matrix
sum = 0
for row in range(NUM_ROWS):
    for column in range(NUM_COLS):
        if row == column:
            sum += my_matrix[row][column]

print(sum)
    
