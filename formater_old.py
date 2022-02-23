import math


class Board:
    """ класс отвечает за взаимодействие с вложенными списками

        ввод и вывод по положению. рисование фигур"""

    def __init__(self):
        self.value = [[" "]*102 + ["\n"]]

    def add_lines(self, arg=1):
        for i in range(0, arg):
            self.value.append([" "]*100 + ["\n"])

    def get_str(self):
        __out = ""
        for line in self.value:
            for sym in line:
                __out += str(sym)
        return __out

    def clear(self):
        self.value = [[" "]*100 + ["\n"]]

    def draw_point(self, __Coordinate,  filler="#"):
        __X, __Y = __Coordinate
        if __Y > len(self.value):
            self.add_lines(__Y - len(self.value))
        self.value[__Y - 1][__X - 1] = filler

    def draw_line(self, __Coordinate1, __Coordinate2, filler="#"):
        __X1, __Y1 = __Coordinate1
        __X2, __Y2 = __Coordinate2
        try:
            __k = (__Y1 - __Y2)/(__X1 - __X2)
        except ZeroDivisionError:
            __k = 0

        __b = __Y2 - __k*__X2
        __x = __X1
        __y = __Y1

        while __x != __X2:  # iteration by X
            __y = round(__k * __x + __b)
            self.draw_point((__x, __y), filler)
            if __X1 <= __X2:
                __x += 1
            elif __X1 >= __X2:
                __x -= 1

        __x = __X1
        __y = __Y1

        while __y != __Y2:  # iteration by Y
            try:
                __x = round((__y-__b)/__k)
            except ZeroDivisionError:
                pass
            self.draw_point((__x, __y), filler)
            if __Y1 <= __Y2:
                __y += 1
            elif __Y1 >= __Y2:
                __y -= 1

        self.draw_point((__X2, __Y2), filler)

    def draw_rectangle(self, __Coordinate1, __Coordinate2, __Coordinate3, filler="▓"):
        __X1, __Y1, __X3, __Y3 = self._unpack_coordinate(__Coordinate1, __Coordinate3)
        __Coordinate4 = (__X1, __Y3)
        self.draw_line(__Coordinate1, __Coordinate2, filler)
        self.draw_line(__Coordinate2, __Coordinate3, filler)
        self.draw_line(__Coordinate3, __Coordinate4, filler)
        self.draw_line(__Coordinate4, __Coordinate1, filler)

    def _draw_text(self, filler, __Coordinate):
        __X, __Y = self._unpack_coordinate(__Coordinate)

        for i in filler:
            self.draw_point((__X, __Y), i)
            __X += 1

    @staticmethod
    def _unpack_coordinate(__Coordinate1, __Coordinate2=None, __Coordinate3=None):
        if __Coordinate2 is None:
            return __Coordinate1[0], __Coordinate1[1]
        elif __Coordinate3 is None and __Coordinate2 is not None:
            return __Coordinate1[0], __Coordinate1[1], __Coordinate2[0], __Coordinate2[1]
        else:
            return __Coordinate1[0], __Coordinate1[1], __Coordinate2[0], __Coordinate2[1], __Coordinate3[0], __Coordinate3[1],

    @staticmethod
    def _count_columns(__filler, __Coordinate1, __Coordinate2):
        __X1, __Y1 = __Coordinate1
        __X2, __Y2 = __Coordinate2

        __columnLen = 25
        __columnNumb = 4

        if len(__filler) < __columnNumb:
            __columnNumb = len(__filler)
        else:
            __columnNumb = (__X2 - __X1 + 1) // __columnLen
        return __columnLen, __columnNumb

    @staticmethod
    def _prepare_list(__filler, __columns):
        __i = 0
        __fillerCopy = __filler[:]

        while True:
            if __i == len(__filler):
                break
            else:
                if len(__filler[__i]) > __columns:

                    __j = 0
                    __saved = __filler[__i][:__columns]
                    del(__filler[__i][:__columns])
                    __filler.insert(__i, __saved)

            __i += 1
        return __filler

    def draw_text_block(self, filler, __Coordinate1, __Coordinate2):
        __X1, __Y1, __X2, __Y2 = self._unpack_coordinate(__Coordinate1, __Coordinate2)

        __div_by_words = tuple(filler.split(" "))
        __line = ""

        for i in __div_by_words:

            if i == "\n":
                self._draw_text(__line, (__X1, __Y1))
                __line = ""
                __Y1 += 1

            elif len(__line + i) > __X2 - __X1 - 2:
                self._draw_text(__line, (__X1, __Y1))
                __line = ""
                __line += " " + i
                __Y1 += 1

            elif len(__line + i) <= __X2 - __X1:
                __line += " " + i

        if __line != " ":
            self._draw_text(__line, (__X1, __Y1))

        return (__Coordinate1[0], __Coordinate1[1]), (__Coordinate2[0], __Coordinate2[1]), (__X2, __Y1)

    def draw_text_rect(self, filler, __Coordinate1, __Coordinate2, __filler="▓"):
        __X1, __Y1, __X2, __Y2 = self._unpack_coordinate(__Coordinate1, __Coordinate2)

        __block = self.draw_text_block(filler, (__X1+1, __Y1+1), (__X2, __Y2+1))
        self.draw_rectangle(__Coordinate1, __Coordinate2, (__block[2][0], __block[2][1]+1), __filler)
        return __block

    def draw_grid(self, __filler, __Coordinate1=(1, 1), __Coordinate2=(100, 1)):

        __X1, __Y1, __X2, __Y2 = self._unpack_coordinate(__Coordinate1, __Coordinate2)

        __columnLen, __columnNumb = self._count_columns(__filler, __Coordinate1, __Coordinate2)

        if len(__filler) < __columnNumb:
            __columnNumb = len(__filler)
        else:
            __columnNumb = (__X2 - __X1 + 1) // __columnLen

        __columnLen = math.floor((__X2 - __X1 + 1) / __columnNumb)
        __maxLineLen = 0

        j = 0
        for i in __filler:

            while True:
                if j < __columnNumb:
                    var = [(__X1 + 2 + __columnLen * j, __Y1+2), (__X1 - 2 + __columnLen * (j + 1), __Y1)]
                    __lineLen = self.draw_text_block(i, var[0], var[1])[2][1]
                    j += 1
                    if __lineLen > __maxLineLen:
                        __maxLineLen = __lineLen + 1
                    break

                else:
                    # переход на новую "линию"

                    for __i in range(0, __columnNumb):
                        __var = [(__X1 + __columnLen * __i, __Y1), (__X1 - 1 + __columnLen * (__i + 1), __Y1)]
                        self.draw_rectangle(__var[0], __var[1], (__var[1][0], __maxLineLen + 1))
                    __Y1 = __maxLineLen + 1
                    j = 0

        for __i in range(0, __columnNumb):
            __var = [(__X1 + __columnLen * __i, __Y1), (__X1 - 1 + __columnLen * (__i + 1), __Y1)]
            self.draw_rectangle(__var[0], __var[1], (__var[1][0], __maxLineLen + 1))
        __Y1 = __maxLineLen + 1
        return __Y1

    def draw_table(self, __filler, __Coordinate1=(1, 1), __Coordinate2=(100, 1)):
        __X1, __Y1, __X2, __Y2 = self._unpack_coordinate(__Coordinate1, __Coordinate2)

        __columnNumb = self._count_columns(__filler, __Coordinate1, __Coordinate2)[1]
        __filler = self._prepare_list(__filler, __columnNumb)

        for i in range(0, len(__filler)):
            for j in __filler:
                while len(__filler[i]) < len(j):
                    __filler[i].append("")
            __Y1 = self.draw_grid(__filler[i], (__X1, __Y1), (__X2, __Y1)) + 1
            self.draw_line((__X1, __Y1), (__X2, __Y1))
