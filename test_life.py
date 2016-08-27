import grid

def test_create_grid():
    A = grid.Grid()
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    A.create_grid(ip)
    assert A.life_grid == ip

def test_is_alive():
    A = grid.Grid()
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    A.create_grid(ip)
    assert A.is_alive(1, 1) == True
    assert A.is_alive(0, 0) == False
    assert A.is_alive(2, 1) == False


def test_num_neighbours():
    A = grid.Grid()
    ip = [[0,0,0], [1,1,1], [1,0,0]]
    A.create_grid(ip)
    """for the cell in the middle"""
    assert A.num_neighbours(1, 1) == 3
    """for the left edge"""
    assert A.num_neighbours(1, 0) == 2
    """for the right edge"""
    assert A.num_neighbours(1, 2) == 1
    """for the top edge"""
    assert A.num_neighbours(0, 1) == 3
    """for the bottom edge"""
    assert A.num_neighbours(2, 1) == 4
    """for the top left corner"""
    assert A.num_neighbours(0, 0) == 2
    """for the top right corner"""
    print (A.num_neighbours(0, 2))
    assert A.num_neighbours(0, 2) == 2
    """for the bottom left corner"""
    assert A.num_neighbours(2, 0) == 2
    """for the bottom right corner"""
    assert A.num_neighbours(2, 2) == 2

def test_kill_cell():
    A = grid.Grid()
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    A.create_grid(ip)
    A.kill_cell(1, 1)
    assert A.is_alive(1, 1) == False
    A.kill_cell(2, 0)
    assert A.is_alive(2, 0) == False
    

def test_birth_cell():
    A = grid.Grid()
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    A.create_grid(ip)
    A.birth_cell(0, 0)
    assert A.is_alive(0, 0) == True
    A.birth_cell(0, 2)
    assert A.is_alive(0, 2) == True
    
    
def test_size():
    A = grid.Grid()
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    A.create_grid(ip)
    assert A.size() == 3

def test_grid_as_array():
    A = grid.Grid()
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    A.create_grid(ip)
    assert len(A.grid_as_array()) == len(ip)
    
def test_apply_rules():
    A = grid.Grid()
    ip = [[0,0,0], [1,1,1], [1,0,0]]
    A.create_grid(ip)
    
    print(A.apply_rules())
    #print (A.life_grid[2][1])
    #print (A.life_grid[1][2])
    assert A.is_alive(0, 1) is True
    assert A.is_alive(1, 2) is False

def test_printme():
    A = grid.Grid()
    ip = [[0,0,0], [1,1,1], [1,0,0]]
    A.create_grid(ip)
    count = 1
    A.printme()
    
    
