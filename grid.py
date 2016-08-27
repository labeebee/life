import copy

class Grid:
    
    life_grid = None

    def create_grid(self, ip):
        # global life_grid
        self.life_grid = copy.deepcopy(ip) # this is used so as to make a copy of the grid

    def is_alive(self, x, y):
        global life_grid
        if self.life_grid[x][y] == 1:
            return True
        else:
            return False
        
    def num_neighbours(self, x, y):
        ncount = 0
        for xn in [x-1, x, x+1]:
            for yn in [y-1, y, y+1]:
                if (xn < 0 or
                    yn < 0 or
                    xn >= len(self.life_grid) or
                    yn >= len(self.life_grid)):
                    pass
                elif xn == x and yn == y:
                    pass
                elif self.is_alive(xn, yn):
                    ncount += 1
        return ncount

    def kill_cell(self, x, y):
        self.life_grid[x][y] = 0 # assigns 0 to the cell being addressed
        # Yes! Literally kills the cell

    def birth_cell(self, x, y): 
        self.life_grid[x][y] = 1 # assigns 1 to the cell being addressed
        # the cell lives

    def size(self): # returns the size of the grid
        # assuming that we are using a square grid, we will have the length of
        # one side returned by this function
        return len(self.life_grid)

    def grid_as_array(self): 
        return self.life_grid

#Layer 1

    def apply_rules(self):
        temp_grid = Grid()
        temp_grid.create_grid(self.life_grid)
        print(temp_grid.life_grid)

        # since we are not actually accessing the values but the indices, I am
        # merely iterating using the position indices and not the grid as such.
        for x in range(0, temp_grid.size()):  # x would vary from 0 to A.size() - 1
            for y in range(0, temp_grid.size()):  # y would vary from 0 to A.size() - 1
                print(x, y)
                if not temp_grid.is_alive(x, y) and temp_grid.num_neighbours(x, y) == 3:
                    print("what is happening here at ({},{}) when num_nei = {}?".format(
                        x, y, temp_grid.num_neighbours(x, y)))
                    self.birth_cell(x, y)
                elif temp_grid.is_alive(x, y) and temp_grid.num_neighbours(x, y) < 2:
                    self.kill_cell(x, y)
                # elif A.is_alive(x, y) and A.num_neighbours(x, y) == (2, 3):
                #     pass
                elif temp_grid.is_alive(x, y) and temp_grid.num_neighbours(x, y) > 3:
                    self.kill_cell(x, y)
                else:
                    pass


    # def printme(self):
        
