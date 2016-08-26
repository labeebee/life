import copy


class Grid:
    def __init__(self, grid):
        self.life_grid = copy.deepcopy(grid)

    def is_alive(self, x, y):
        return self.life_grid[x][y] == 1

    def num_neighbours(self, x, y):
        ncount = 0
        for xn in [x-1, x, x+1]:
            for yn in [y-1, y, y+1]:
                if (xn < 0 or yn < 0 or
                   xn >= len(self.life_grid) or
                   yn >= len(self.life_grid)):
                    pass
                elif xn == x and yn == y:
                    pass
                elif self.is_alive(xn, yn):
                    ncount += 1
        return ncount

    def kill_cell(self, x, y):
        self.life_grid[x][y] = 0

    def birth_cell(self, x, y):
        self.life_grid[x][y] = 1

    def size(self):
        return len(self.life_grid)

    def grid_as_array(self):
        return self.life_grid

    def apply_rules(self):
        curr_grid = Grid(self.life_grid)
        print(curr_grid.life_grid)

        # since we are not actually accessing the values but the indices, I am
        # merely iterating using the position indices and not the grid as such.
        for x in range(0, curr_grid.size()):  # x would vary from 0 to A.size() - 1
            for y in range(0, curr_grid.size()):  # y would vary from 0 to A.size() - 1
                print(x, y)
                if not curr_grid.is_alive(x, y) and curr_grid.num_neighbours(x, y) == 3:
                    print("what is happening here? {}{} when num_nei = {}".format(
                        x, y, curr_grid.num_neighbours(x, y)))
                    self.birth_cell(x, y)
                elif curr_grid.is_alive(x, y) and curr_grid.num_neighbours(x, y) < 2:
                    self.kill_cell(x, y)
                # elif A.is_alive(x, y) and A.num_neighbours(x, y) == (2, 3):
                #     pass
                elif curr_grid.is_alive(x, y) and curr_grid.num_neighbours(x, y) > 3:
                    self.kill_cell(x, y)
                else:
                    pass
