def check_coordinates(*args):
    """ check coordinates on positive int
    """
    out = []
    for item in args:
        # checking len of coordinate and add '#' if needed
        if len(item) == 2:
            item += ("#", )
        # checking type and length of filler
        if len(item) == 3:
            if len(item[2]) != 1 or type(item[2]) != str:
                raise ValueError('\n\n\tIncorrect filler.\n')
        else:
            raise ValueError ('\n\n\tuncorrect coordinate given!'+
                ' it supposed to have 2 or 3 elements.\n')
        # checking type of cioordinate items
        if (type(item[0]) == int and
                item[0] > 0 and
                type(item[1]) == int and
                item[1] > 0):
                out.append(item)
        else:
            raise ValueError('\n\n\tuncorrect coordinate given!'+
            ' its supposed to be positive int.\n')
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
        # (y1 - y2)x + (x2 - x1) y + (x1y2 - x2y1) = 0 -- каноническое
        # уравнение приведённое к виду общего уравнения
        # x = -(By + C)/ A
        # y = -(Ax + C)/ B
    A = Y1 - Y2
    B = X2 - X1
    C = X1 * Y2 - X2 * Y1
    # script calculates variables through x
    while y != Y2:
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
    while x != X2:
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
    grid.update([( (X2,Y2), c1[2] )])
    return grid

def assembly(grid):
    """ compile values from dict to string by lists
    """
    #variables for dict-list and list-str conversion list needed to save state
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
    # temp variables for converting
    tmp = ""
    tmp2 = ""
    # convert list to string
    for i in out:
        tmp = tmp2.join(i)
        out_ += tmp + '\n'
    return out_

def draw_text_container(c1, c2, text, wrapping = True, grid = None ):
    """ input text in rectangle block with 2 coordinates - upper left corner
        and upper rigth corner. wrap words in default
    """
    # raise error if wrong input
    if c1[0] == c2[0]:
        raise ValueError('\n\n\tYour text block can\'t have zero length!\n')
    c1, c2 = check_coordinates(c1,c2)
    if grid == None:
        grid = {}
    # flips coordinates, if c1 is right corner instead be left corner
    if c1 > c2:
        c1, c2 = c2, c1
    # carriage coordinates
    x = c1[0]
    y = c1[1]
    splited = list(text.split(" "))
    container = c2[0] - c1[0] + 1
    for word in splited:
        # carriage wrap if needed
        # if word bigger then container, do nothing
        if len(word) > c2[0] - x + 1  and len(word) <= container:
            y += 1
            x = c1[0]

        # new string
        if word == "\n":
            y += 1
            x = c1[0]
            continue
        # tabulation if enough space
        elif word == "\t" and c2[0] - x + 1 >= 4:
            for i in range(0,4):
                grid.update([( (x+i,y), " " )])
            x += 4
            continue
        # tabulation if not enough space
        elif word == "\t" and not c2[0] - x + 1 >= 4:
            y += 1
            for i in range(0,4):
                grid.update([( (x+i,y), " " )])
            x = c1[0]
            continue
        # word if words length less or equal container
        elif len(word) <= container:
            for j in range(0,len(word)):
                grid.update([( (x,y), word[j] )])
                x += 1
        # word if words longer than container
        elif len(word) > container:
                    #  may be it better to rework thise func
            # divade word into parts
            parts = [word[:c2[0]-x:]]
            word = word[c2[0]-x:]
            # continue divading
            while len(word) > container:
                parts += [word[:container]]
                word = word[container:]
            if len(word) >= 1:
                parts += [word]
            for part in parts:
                for char in part:
                    grid.update([( (x,y), char )])
                    x += 1
                x = c1[0]
                y += 1
        # add " " after word. skipped, if word is special char
        if x != c2[0]:
            grid.update([( (x,y), " " )])
            x +=1
    return grid
