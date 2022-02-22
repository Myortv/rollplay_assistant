def check_coordinates(*args):
    """ check coordinates on positive int
    """
    for item in args:
        print(item[0].type())
        if item[0].type() == 'int' and item[0] >= 0 and item[1].type() == 'int' and item[1] >= 0:
            return True
        else:
            raise ValueError('uncorrect coordinate! it must be positive int')

def draw_point(c1, grid = None):
    """ add point to grid
    """
    check_coordinates(c1)
    if grid == None:
        grid = set()
    return grid.add(c1)

def grid_to_str(grid):
    out = [" ",]
    out_=""
    for i in grid:
        y = i[1]
        x = i[0]
        if len(out) < y:
            out += ' ' * (y - len(out))
        if out[y].len() < x:
            out[y]+=' ' * (x - len(out[y]))

        out[y][x] = i[3] or '#'
        out[y] += ' '

    for i in out:
        out_ += i + '\n'
