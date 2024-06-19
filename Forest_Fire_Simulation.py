import random
import json

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def initialize_grid(height, width, initial_fires):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for fire in initial_fires:
        grid[fire[0]][fire[1]] = 'F'
    return grid

def display_grid(grid):
    for row in grid:
        print(' '.join(row))
    print('\n')

def spread_fire(grid, probability):
    height = len(grid)
    width = len(grid[0])
    new_grid = [row[:] for row in grid]
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'F':
                new_grid[i][j] = 'C'
                if i > 0 and grid[i-1][j] == '.' and random.random() < probability:
                    new_grid[i-1][j] = 'F'
                if i < height - 1 and grid[i+1][j] == '.' and random.random() < probability:
                    new_grid[i+1][j] = 'F'
                if j > 0 and grid[i][j-1] == '.' and random.random() < probability:
                    new_grid[i][j-1] = 'F'
                if j < width - 1 and grid[i][j+1] == '.' and random.random() < probability:
                    new_grid[i][j+1] = 'F'
    return new_grid

def is_fire_present(grid):
    for row in grid:
        if 'F' in row:
            return True
    return False

def main():
    config = read_config('config.json')
    height = config['height']
    width = config['width']
    initial_fires = config['initial_fires']
    probability = config['probability']
    
    grid = initialize_grid(height, width, initial_fires)
    step = 0
    
    while is_fire_present(grid):
        print(f"Step {step}")
        display_grid(grid)
        grid = spread_fire(grid, probability)
        step += 1
    
    print("Final State")
    display_grid(grid)

if __name__ == "__main__":
    main()
