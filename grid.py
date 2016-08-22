life_grid = None

def create_grid(ip):
    global life_grid
    life_grid = ip

def is_alive(x,y):
    if life_grid[x][y] == 1:
        return True
    else:
        return False
