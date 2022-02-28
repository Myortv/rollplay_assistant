def check_coordinates(*args):
    """ check coordinates on positive int
    """
    out = []
    for item in args:
        # checking len of coordinate and add '#' if needed
        if len(item) == 2:
            item += ("#", )
        else:
            raise ValueError ('uncorrect coordinate given! it supposed to have 2 or 3 elements.')
        # checking type of cioordinate items
        if (type(item[0]) == int and
                item[0] > 0 and
                type(item[1]) == int and
                item[1] > 0):
                out.append(item)
        else:
            raise ValueError('uncorrect coordinate given! its supposed to be positive int.')
    # return the only one value, if thise possible
    if len(out) == 1:
        return out[0]
    return out

def draw_point(c1, grid = None):
    """ add point to grid
    """
    c1 = check_coordinates(c1)
    if grid == None:
        grid = {}
    grid.update([( (c1[:2]), c1[2] )])
    return grid

def draw_line(c1, c2, grid = None):
    """ calculate points on line and add to grid
    """
    c1, c2 = check_coordinates(c1,c2)
    if grid == None:
        grid = {}
    # readable immutable coordinates
    X1 = c1[0]
    X2 = c2[0]
    Y1 = c1[1]
    Y2 = c2[1]
    # mutable variables for ging through cycle
    x = c1[0]
    y = c1[1]
    # math constant
        # Ax + Bx + C = 0  -- общее уравнение прямой
        # (y1 - y2)x + (x2 - x1) y + (x1y2 - x2y1) = 0 -- каноническое уравнение
        # приведённое к виду общего уравнения
        # x = -(By + C)/ A
        # y = -(Ax + C)/ B
    A = Y1 - Y2
    B = X2 - X1
    C = X1 * Y2 - X2 * Y1
    # script calculates variables through x
    while x != X2:
        try:
            x = round( -(B * y + C)/ A )
        except ZeroDivisionError:
            break
        grid.update([( (x,y), c1[2] )])
        # stepping by y
        if Y1 <= Y2:
            y += 1
        else:
            y -= 1
    # refresh variables
    x = c1[0]
    y = c1[1]
    # script calculates coordinates through y
    while y != Y2:
        try:
            y = round( -(A * x + C )/ B)
        except ZeroDivisionError:
            break
        grid.update([( (x,y), c1[2] )])
        # stepping by x
        if X1 <= X2:
            x += 1
        else:
            x -= 1
    # drawing endpoint
    grid = _draw_point((X2,Y2,c1[2]), grid)
    return grid

def assembly(grid):
    """ compile values from dict to string by lists
    """
    # variables for dict-list and list-str conversion list needed to save state
    out = [[' ']]
    out_ = ""
    # going through grid coordinates to make list
    for i in grid:
        x = i[0]
        y = i[1]
        # add blank lines [' ']
        if len(out) < y:
            out += [[" "]] * (y - len(out))
        # add blank char in line if needed
        if len(out[y-1]) < x:
            out[y-1] += [' '] * (x - len(out[y-1]))
        # add char from greed
        out[y-1][x-1] = grid[i]
    # convert list to string
    tmp = ""
    tmp2 = ""
    for i in out:
        tmp = tmp2.join(i)
        out_ += tmp + '\n'
    return out_

print(assembly(draw_line((1,1), (44,10))))
