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

def birth_cell(x,y):
    life_grid[x][y] = 1

def size():
    return len(life_grid)

def grid_as_array():
    return life_grid
