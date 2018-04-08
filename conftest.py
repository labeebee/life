import pytest

import grid


@pytest.fixture()
def get_grid():
    def created_grid(ip):
        A = grid.Grid()
        A.create_grid(ip)
        return A

    return created_grid
