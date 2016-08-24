life_grid = None

def create_grid(ip):
    global life_grid
    life_grid = ip

def is_alive(x,y):
    if life_grid[x][y] == 1:
        return True
    else:
        return False
def num_neighbours(x,y):
    ncount = 0
    for xn in [x-1, x, x+1]:
        for yn in [y-1, y, y+1]:
            if xn < 0 or yn < 0 or xn >= len(life_grid) or yn >= len(life_grid):
                pass
            elif xn == x and yn == y:
                pass
            elif (is_alive(xn,yn) == True):
                ncount += 1
    return ncount

def kill_cell(x, y):
    life_grid[x][y] = 0

def birth_cell(x, y):
    life_grid[x][y] = 1

def size():
    return len(life_grid)

def grid_as_array():
    return life_grid

#Layer 1

def apply_rules():
    for x in range(0, size()):
        for y in range(0, size()):
            if is_alive(x, y) and num_neighbours(x, y) < 2:
                kill_cell(x, y)
            elif is_alive(x, y) and num_neighbours(x, y) == (2, 3):
                pass
            elif is_alive(x, y) and num_neighbours(x, y) > 3:
                kill_cell(x, y)
            elif is_alive(x, y) and num_neighbours == 3:
                birth_cell(x, y)





