def tower(height, from_column, to_column, tmp_column):
    if height == 1:
        print(f'From {from_column} to {to_column}')
    else:
        tower(height-1, from_column, tmp_column, to_column)
        print(f'From {from_column} to {to_column}')
        tower(height-1, tmp_column, to_column, from_column)

tower(4, 'A', 'B', 'C')
