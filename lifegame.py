import copy
import os
import time

def create_grid(rows,cols):
    grid=[]
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(0)
        grid.append(row)
    return grid


def place_cell(grid, coord):
    i_row = coord[0]
    i_col = coord[1]
    grid[i_row][i_col] = 1


def display(grid):
    grid_displayed = ""
    for row in grid:
        line = ""
        for cell in row:
            if cell == 1:
                line += "\u25A0"
            else:
                line +="."
        line += "\n"
        grid_displayed += line
    print(grid_displayed)

def count_neighbors(grid, coord):
    count = 0
    i_row = coord[0]
    i_col = coord[1]
    for row in range(i_row-1,i_row+2):
        for col in range(i_col-1,i_col+2):
            if (row == i_row and col == i_col) or row<0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            count += grid[row][col]
    return count

def update(grid):
    new_grid= copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count = count_neighbors(grid,(row,col))
            if grid[row][col] == 1:
                if(count != 3 and count !=2):
                    new_grid[row][col]=0
            else:
                if count == 3:
                    new_grid[row][col] = 1
    return new_grid


def run_game():
    grid = create_grid(5,5)
    place_cell(grid,(1,2))
    place_cell(grid,(2,2))
    place_cell(grid,(3,2))
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        display(grid)
        grid = update(grid)
        time.sleep(0.5)

run_game()