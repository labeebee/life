import grid


def test_create_grid():
    ip = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    assert A.life_grid == ip


def test_is_alive():
    ip = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    assert A.is_alive(1, 1)
    assert not A.is_alive(0, 0)
    assert not A.is_alive(2, 1)


def test_num_neighbours():
    ip = [
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    # For the cell in the middle
    assert A.num_neighbours(1, 1) == 3
    """for the left edge"""
    assert A.num_neighbours(1, 0) == 2, 'Left edge neighbour missing'
    """for the right edge"""
    assert A.num_neighbours(1, 2) == 1
    """for the top edge"""
    assert A.num_neighbours(0, 1) == 3
    """for the bottom edge"""
    assert A.num_neighbours(2, 1) == 4
    """for the top left corner"""
    assert A.num_neighbours(0, 0) == 2
    """for the top right corner"""
    print(A.num_neighbours(0, 2))
    assert A.num_neighbours(0, 2) == 2
    """for the bottom left corner"""
    assert A.num_neighbours(2, 0) == 2
    """for the bottom right corner"""
    assert A.num_neighbours(2, 2) == 2


def test_kill_cell():
    ip = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    A.kill_cell(1, 1)
    assert not A.is_alive(1, 1)
    A.kill_cell(2, 0)
    assert not A.is_alive(2, 0)


def test_birth_cell():
    ip = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    A.birth_cell(0, 0)
    assert A.is_alive(0, 0)
    A.birth_cell(0, 2)
    assert A.is_alive(0, 2)


def test_size():
    ip = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    assert A.size() == 3


def test_grid_as_array():
    ip = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    assert len(A.grid_as_array()) == len(ip)


def test_apply_rules():
    ip = [
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
    ]
    A = grid.Grid(ip)
    print(A.life_grid)
    print("the number of neighbours is {}".format(A.num_neighbours(2, 1)))
    # assert A.is_alive (2, 1) == False
    print(A.apply_rules())
    # print(A.life_grid[2][1])
    # print(A.life_grid[1][2])
    assert A.is_alive(0, 1)
    assert not A.is_alive(1, 2)
