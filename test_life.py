import grid

def test_create_grid():
    """Makes sure that the input is stored inside the grid module as 
life_grid"""
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    grid.create_grid(ip)
    assert grid.life_grid == ip


def test_is_alive ():
    """ This tests, for the given position if the cell is alive True if alive, false otherwise. """

    ip = [[0,0,0], [0,1,1], [1,0,0]]
    assert grid.is_alive(1, 1) == True
    assert grid.is_alive(0, 0) == False

def test_num_neighbours():
    """This tests the number of neighbours function for a given position"""
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    """for the cell in the middle"""
    assert grid.num_neighbours(1, 1) == 2
    """for the left edge"""
    assert grid.num_neighbours(1, 0) == 2
    """for the right edge"""
    assert grid.num_neighbours(1, 2) == 1
    """for the top edge"""
    assert grid.num_neighbours(0, 1) == 2
    """for the bottom edge"""
    assert grid.num_neighbours(2, 1) == 3
    """for the top left corner"""
    assert grid.num_neighbours(0, 0) == 1
    """for the top right corner"""
    assert grid.num_neighbours(0, 2) == 2
    """for the bottom left corner"""
    assert grid.num_neighbours(2, 0) == 1
    """for the bottom right corner"""
    assert grid.num_neighbours(2, 2) == 2
    
    
    
    
