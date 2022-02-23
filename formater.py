def check_coordinates(*args):
    """ check coordinates on positive int
    """
    for item in args:
        if type(item[0]) == int and item[0] > 0 and type(item[1]) == int and item[1] > 0:
            return True
        else:
            raise ValueError('uncorrect coordinate! it must be positive int')

def draw_point(c1, grid = None):
    """ add point to grid
    """
    check_coordinates(c1)
    if grid == None:
        grid = set()
    if len(c1) == 2:
        c1 += ("#",)
    grid.add(c1)
    return grid


def grid_to_str(grid):
    """
    """
    out = [[' ']]
    out_=""
    for i in grid:
        y = i[1]
        x = i[0]
        while len(out) < y:
            # add lines
            out += [[" "]]

        # print(i)
        # print(len(out[y-1]))
        if len(out[y-1]) < x:
            # add x pos in line
            out[y-1] += [' '] * (x - len(out[y-1]))
        out[y-1][x-1] = i[2]

    for i in out:
        for j in i:
            out_ += j
        else:
            out_ += '\n'
    return out_
