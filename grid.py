class Grid:
    life_grid = None

    def create_grid(self, ip):
        global life_grid
        self.life_grid = ip

    def is_alive(self, x, y):
        global life_grid
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


# Layer 1
def apply_rules(A):
    B = Grid()
    B.create_grid(A.life_grid)
    print(B.life_grid)
    # since we are not actually accessing the values but the indices, I am
    # merely iterating using the position indices and not the grid as such.
    for x in range(0, A.size()):  # x would vary from 0 to A.size() - 1
        for y in range(0, A.size()):  # y would vary from 0 to A.size() - 1
            print(x, y)
            if not A.is_alive(x, y) and A.num_neighbours(x, y) == 3:
                print("what is happening here? {}{} when num_nei = {}".format(
                    x, y, A.num_neighbours(x, y)))
                B.birth_cell(x, y)
            elif A.is_alive(x, y) and A.num_neighbours(x, y) < 2:
                B.kill_cell(x, y)
            # elif A.is_alive(x, y) and A.num_neighbours(x, y) == (2, 3):
            #     pass
            elif A.is_alive(x, y) and A.num_neighbours(x, y) > 3:
                B.kill_cell(x, y)
            else:
                pass

            # if not A.is_alive(x, y) and A.num_neighbours(x, y) == 3:
            #     print("This is {}{}".format(x, y))
            #     print(A.is_alive(x, y))
            #     print(A.num_neighbours(x, y))
            #     B.birth_cell(x, y)
            #     break
    A.life_grid = B.life_grid
    return A.life_grid
