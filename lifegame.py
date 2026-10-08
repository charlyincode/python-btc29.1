def create_grid(rows,cols):
    grid=[]
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(0)
        grid.append(row)
    return grid

grid = create_grid(5,5)

def place_cell(grid, coord):
    i_row = coord[0]
    i_col = coord[1]
    grid[i_row][i_col] = 1

place_cell(grid,(2,1))

def display(grid):
    grid_displayed = ""
    for row in grid:
        line = ""
        for cell in row:
            line +="."
        line += "\n"
        grid_displayed += line
    print(grid_displayed)

display(grid)