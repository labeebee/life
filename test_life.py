import grid

def test_create_grid():
    """Makes sure that the input is stored inside the grid module as 
life_grid"""
    ip = [[0,0,0], [0,1,1], [1,0,0]]
    grid.create_grid(ip)
    assert grid.life_grid == ip
