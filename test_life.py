import pytest

import grid

STANDARD_GRID = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]


def test_create_grid():
    A = grid.Grid()
    ip = STANDARD_GRID
    A.create_grid(ip)
    assert A.life_grid == ip


def test_is_alive(get_grid):
    A = get_grid(STANDARD_GRID)
    assert A.is_alive(1, 1) is True
    assert A.is_alive(0, 0) is False
    assert A.is_alive(2, 1) is False


@pytest.mark.parametrize(
        'x,y,result',
        [(1, 1, 3), (1, 0, 2), (1, 2, 1), (0, 1, 3), (2, 1, 4), (0, 0, 2), (0, 2, 2),
         (2, 0, 2), (2, 2, 2)],
        ids=['Middle', 'Left Edge', 'Right Edge', 'Top Edge', 'Bottom Edge', 'TL Corner', 'TR Corner',
             'BL Corner', 'BR Corner'])
def test_num_neighbours(x, y, result, get_grid):
    A = get_grid([[0, 0, 0], [1, 1, 1], [1, 0, 0]])
    assert A.num_neighbours(x, y) == result


def test_kill_cell(get_grid):
    A = get_grid(STANDARD_GRID)
    A.kill_cell(1, 1)
    assert A.is_alive(1, 1) is False
    A.kill_cell(2, 0)
    assert A.is_alive(2, 0) is False


def test_birth_cell(get_grid):
    A = get_grid(STANDARD_GRID)
    A.birth_cell(0, 0)
    assert A.is_alive(0, 0) is True
    A.birth_cell(0, 2)
    assert A.is_alive(0, 2) is True


def test_size(get_grid):
    A = get_grid(STANDARD_GRID)
    assert A.size() == 3


def test_grid_as_array(get_grid):
    A = get_grid(STANDARD_GRID)
    assert len(A.grid_as_array()) == len(STANDARD_GRID)


def test_apply_rules(get_grid):
    A = get_grid([[0, 0, 0], [1, 1, 1], [1, 0, 0]])

    print(A.apply_rules())
    # print (A.life_grid[2][1])
    # print (A.life_grid[1][2])
    assert A.is_alive(0, 1) is True
    assert A.is_alive(1, 2) is False


def test_printme(get_grid):
    A = get_grid([[0, 0, 0], [1, 1, 1], [1, 0, 0]])
    count = 1
    print(A.printme())
