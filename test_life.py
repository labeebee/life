import grid

A = grid.Grid()
ip = None
def test_create_grid():
    global ip
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    A.create_grid(ip)
    assert A.life_grid == ip

def test_is_alive():
    assert A.is_alive(1, 1) == True
    assert A.is_alive(0, 0) == False
    assert A.is_alive(2, 1) == False


def test_num_neighbours():
    """for the cell in the middle"""
    assert A.num_neighbours(1, 1) == 2
    """for the left edge"""
    assert A.num_neighbours(1, 0) == 2
    """for the right edge"""
    assert A.num_neighbours(1, 2) == 1
    """for the top edge"""
    assert A.num_neighbours(0, 1) == 2
    """for the bottom edge"""
    assert A.num_neighbours(2, 1) == 3
    """for the top left corner"""
    assert A.num_neighbours(0, 0) == 1
    """for the top right corner"""
    assert A.num_neighbours(0, 2) == 2
    """for the bottom left corner"""
    assert A.num_neighbours(2, 0) == 1
    """for the bottom right corner"""
    assert A.num_neighbours(2, 2) == 2

def test_kill_cell():
    A.kill_cell(1, 1)
    assert A.is_alive(1, 1) == False
    A.kill_cell(2, 0)
    assert A.is_alive(2, 0) == False

def test_birth_cell():
    A.birth_cell(0, 0)
    assert A.is_alive(0, 0) == True
    A.kill_cell(0, 0)
    A.birth_cell(0, 2)
    assert A.is_alive(0, 2) == True
    A.kill_cell(0, 2)
    
    
def test_size():
    assert A.size() == 3

def test_grid_as_array():
    assert len(A.grid_as_array()) == len(ip)
    
def test_apply_rules():
    print (A.life_grid[2][1])
    print (A.life_grid[1][2])  
    grid.apply_rules(A)
    print (A.life_grid[2][1])
    print (A.life_grid[1][2])
    assert A.is_alive(2, 1) == True
    assert A.is_alive(1, 2) == False
    
