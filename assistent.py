import os
import json
import random
import formater
from abc import ABC, abstractmethod


class Primitive:

    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename
        self.value = []
        self.fileId = os.fsencode(filepath + filename)
        self.outId = os.fsencode("output/" + filename+".txt")

        if not os.access(self.fileId, os.F_OK):
            try:
                os.makedirs(os.fsencode(self.filepath))
            except FileExistsError:
                pass

            __tempfile = open(self.fileId, "w")
            __tempfile.write("[]")
            __tempfile.close()

    def open(self):
        with open(self.fileId, "r") as opened_file:
            self.value = json.load(opened_file)

    def save(self):
        with open(self.fileId, "w") as opened_file:
            json.dump(self.value, opened_file)

    def get_rand_item(self):
        self.open()
        return random.choice(self.value)

    def add(self, __inputitem):
        self.open()
        self.value.append(__inputitem)
        self.save()

    def input(self):
        __c = 0

        while True:
            __c += 1
            __inputitem = input(f"[{__c}] Add in [{self.filename}]> ")

            if __inputitem == "":
                break

            else:
                self.add(__inputitem)

    def display(self):
        self.open()
        for i in self.value:
            print(i)

    def edit(self, __targ, __replacement):
        self.open()

        if __targ in self.value:
            __index = self.value.index(__targ)
            self.value.remove(__targ)
            self.value.insert(__index, __replacement)
            self.save()

    def clear(self):
        self.value = []
        self.save()

    def out(self):
        self.open()
        with open(self.outId, "w") as opened_file:
            opened_file.write(str(self.value))

    def _out_in_file(self, __out):
        with open(self.outId, "w") as opened_file:
            opened_file.write(__out)


class Catalog(Primitive, ABC):

    def __init__(self, filepath, filename):
        super().__init__(filepath, filename)

    @property
    @abstractmethod
    def resoursesPath(self):
        """ Path-like for generate method """
        pass

    @property
    @abstractmethod
    def inputExeptions(self):
        """ list of categories exeption, that not includes in sourses file"""
        pass

    @property
    @abstractmethod
    def inputCategories(self):
        """ categories for beautiful input in __input_item """
        pass

    @abstractmethod
    def generate(self):
        """ generate a catalog from default resourses, uses resoursesPath.

            resoursesPath is path for default resourses."""
        pass

    @abstractmethod
    def out(self):
        """return user-frendly formated data(self.value)"""
        pass

    def input_item(self):
        print()
        __out = [input(f"[input {self.inputCategories[0]}]> ")]
        __sourse_file = Primitive(self.filepath + f"{self.filename}_sourse/", __out[0])
        __sourse_file.add(__out[0])
        for __i in self.inputCategories[1:]:
            __inputItem = input(f"[input \"{__i}\" in \"{__out[0]}\"]> ")

            if __inputItem != "$":
                __out.append(__inputItem)

                if __i not in self.inputExeptions:
                    __sourse_file.add(__inputItem)
                    __sourse_file.save()
                else:
                    __sourse_file.add("---")
                    __sourse_file.save()
            else:
                print("#" * 20)
                break

        return __out

    def input(self, catType=""):

        while True:
            __out = []
            __inputitem = input(f"[input / for start]> ")
            if __inputitem == "/":
                self.add(__out + (self.input_item()))

            elif __inputitem == "$":
                break
            else:
                self.add(__inputitem)

    def make(self, __dir):
        self.clear()
        listx = os.listdir(__dir)
        for i in listx:
            if os.path.isfile(__dir + i):
                file = Primitive(__dir, i)
                file.open()
                self.add(file.value)

    def edit(self):
        self.open()
        key = 0
        __target = input("[input target tittle]> ")
        __copy = self.value[:]

        if key == 0:
            __target_cat = input("[input category]> ")
        else:
            __target_cat = "$"

        for i in range(0, len(self.value)):

            if __target in self.value[i]:
                if __target_cat == "$":
                    __copy.pop(i)
                    __copy.insert(i, self.input_item())
                    break
                elif __target_cat in self.inputCategories:
                    __target_cat = self.inputCategories.index(__target_cat)
                    __copy[i].pop(__target_cat)
                    __copy[i].insert(__target_cat, input(f"[input \"{self.inputCategories[__target_cat]}\" in \"{__target}]\">"))
                    print(__copy[i][__target_cat])
                    break
                else:
                    print("\t ERROR(UNCORRECT CATEGORY INPUTED)")
                    return 0

        self.value = __copy
        self.save()

    def sort_by(self, __category, __filter):
        self.open()
        __category = self.inputCategories.index(__category)
        __out = []
        for i in range(0, len(self.value)):
            if __filter in self.value[i][__category]:
                __out.append(self.value[i])
        return __out


class Inventory(Catalog):

    @property
    def resoursesPath(self):
        return os.fsencode(".resourses/inventory/")

    @property
    def inputExeptions(self):
        return ["None"]

    @property
    def inputCategories(self):
        return ["Title", "Category", "Grade", "Set", "Discription", "Master Discription",
                "Amount", "Comments"]

    def random_item(self, __grade=0, __spreading=2):
        self.open()
        if __grade == 0:
            return random.choice(self.value)

        else:
            __bottom, __top = __grade, __grade
            while True:
                if random.randint(1, __spreading) == 1:
                    while True:
                        randName = random.choice(self.value)
                        if int(randName[1]) in range(__bottom, __top + 1):
                            return randName

                        else:
                            break
                else:
                    if __bottom > 0:
                        __bottom -= 1

                    if __top < 11:
                        __top += 1

    def generate(self, __grade=3):
        self.open()
        __out = []
        for i in range(0, 3 * __grade):
            __out.append(self.random_item(__grade))
        return __out

    def __get_head(self):
        board = formater.Board()
        board.draw_text_block(f"[{self.filename.upper()}]", (1, 1), (100, 1),)
        board.add_lines()

        return board.get_str()

    def __get_item_list(self):
        board = formater.Board()
        self.open()
        board.draw_text_block("ITEM LIST (name and amount of all items you have)", (5, 1), (100, 1))
        __out = []
        for i in self.value:
            if type(i) == list:
                __temp = f"•{i[0]} \n •{i[1]} \n \n amount:{i[6]} \n Index: {self.value.index(i) + 1}"
                __out.append(__temp)
            else:
                __temp = i
                __out.append(i)
        board.draw_grid(__out, (1, 2), (100, 2))
        board.add_lines()

        return board.get_str()

    def __get_item_cards(self, key=1):

        board = formater.Board()
        self.open()
        board.draw_line((1, 1), (100, 1), "•")
        __Ylines = 1

        for i in self.value:
            if type(i) == list:
                __temp = f"Name: {i[0]} \n Type: {i[1]} \n Amount: {i[6]}"
                __Y1 = board.draw_text_block(__temp, (2, 3 + __Ylines), (25, 3 + __Ylines))[2][1]

                if key == 1:
                    __temp = f"Discription: {i[4]} \n \n Comment: {i[7]}"
                elif key == 2:
                    __temp = f"Discription: {i[4]} \n \n Set: {i[3]} \n \n Comment: {i[7]}"
                elif key == 3:
                    __temp = f"Discription: {i[4]} \n \n Master Discription: {i[5]}"
                    __temp += " \n \n Grade: {i[2]} \n \n Set: {i[3]} \n \n Comment: {i[7]} "

                __Y2 = board.draw_text_block(__temp, (29, 2 + __Ylines), (100, 2 + __Ylines))[2][1]

                __Y = __Ylines
                if __Y1 + 1 >= __Y2:
                    __Ylines = __Y1 + 3
                    board.draw_text_rect(f"{self.value.index(i) + 1}", (1, __Ylines - 1), (8, __Ylines - 1))
                else:
                    __Ylines = __Y2 + 1
                    board.draw_text_rect(f"{self.value.index(i) + 1}", (1, __Ylines - 1), (8, __Ylines - 1))

                board.draw_rectangle((1, 1 + __Y), (26, 1 + __Y), (26, 1 + __Ylines))
                board.draw_line((29, 2 + __Y), (29, __Ylines - 1), "|")
            else:
                pass

        return board.get_str()

    def out(self, key=0):
        __out = self.__get_head()
        __out += self.__get_item_list()
        if key > 0:
            __out += self.__get_item_cards(key)

        self._out_in_file(__out)

    def get_inventory(self, key=1):
        __out = self.__get_head()
        __out += self.__get_item_list()
        if key > 0:
            __out += self.__get_item_cards(key)

        return __out


class Pool(Catalog):

    @property
    def resoursesPath(self):
        return os.fsencode(".resourses/skills/")

    @property
    def inputExeptions(self):
        return ["None"]

    @property
    def inputCategories(self):
        return ["Title", "Category", "Active Points", "Passive Points",
                "Book points", "Discription", "Bonus Discription", "Master Discription",
                "Comments"]

    def generate(self, __grade=3):
        return 0

    def get_head(self):
        board = formater.Board()
        self.open()
        __allPoints = 0

        board.draw_text_block(f"▐- {self.filename.upper()}", (25, 2), (100, 2))
        board.draw_point((26, 3), "▐")
        board.draw_line((27, 3), (45 + random.randint(1, 50), 3), "▀")
        board.draw_line((1, 4), (100, 4), "░")
        board.draw_line((1, 7), (100, 7), "░")
        board.draw_line((65, 7), (65, 4), "▒")
        board.draw_line((64, 7), (64, 4), "▒")

        for i in self.value:
            if type(i) == list and len(i) == len(self.inputCategories):
                __allPoints += int(i[2]) + int(i[3]) + int(i[4])  # связать с inputCategories

        __top = round(__allPoints / len(self.value) * 10)
        if __top > 100:
            __top = 100

        for i in range(1, __top):
            board.draw_point((i, 5), "▓")
            board.draw_point((i, 6), "▓")
        board.add_lines()

        return board.get_str()

    def __get_skills_cards(self, key=1):

        board = formater.Board()
        self.open()
        board.draw_line((1, 1), (100, 1), "•")
        __Ylines = 0

        for skill in self.value:
            if type(skill) == list and len(skill) == len(self.inputCategories):

                __temp = f"•{skill[0]} \n {skill[1]} \n \n \n \n {skill[-1]}"

                __Y1 = board.draw_text_block(__temp, (5, 4 + __Ylines), (25, 4 + __Ylines))[2][1]
                if __Y1 < 10 + __Ylines:
                    __Y1 = 10 + __Ylines

                board.draw_rectangle((4, 2 + __Ylines), (24, 2 + __Ylines), (24, __Y1 + 1), "▒")
                board.draw_rectangle((35, 2 + __Ylines), (56, 2 + __Ylines), (56, 4 + __Ylines), "░")
                board.draw_rectangle((60, 2 + __Ylines), (73, 2 + __Ylines), (73, 4 + __Ylines), "░")
                board.draw_rectangle((76, 2 + __Ylines), (85, 2 + __Ylines), (85, 4 + __Ylines), "░")

                for __i in range(0, 5):
                    if __i in range(0, int(skill[2])):
                        __filler = "▓"
                    else:
                        __filler = "-"
                    board.draw_point((37 + 4*__i, 3 + __Ylines), __filler)
                    board.draw_point((38 + 4*__i, 3 + __Ylines), __filler)

                for __i in range(0, 3):
                    if __i in range(0, int(skill[3])):
                        __filler = "▓"
                    else:
                        __filler = "-"
                    board.draw_point((62 + 4*__i, 3 + __Ylines), __filler)
                    board.draw_point((63 + 4*__i, 3 + __Ylines), __filler)

                for __i in range(0, 2):
                    if __i in range(0, int(skill[4])):
                        __filler = "▓"
                    else:
                        __filler = "-"
                    board.draw_point((78 + 4*__i, 3 + __Ylines), __filler)
                    board.draw_point((79 + 4*__i, 3 + __Ylines), __filler)

                if key == 1:
                    __temp = f"DESCRIPTION: {skill[5]} \n \n BONUS DISCRIPTION"
                    __temp +=f"{skill[6]} \n \n СOMMENT: {skill[-1]} \n \n"
                elif key == 3 or key == 2:
                    __temp = f"DISCRIPTION: {skill[5]} \n \n BONUS DISCRIPTION: "
                    __temp += f"{skill[6]} \n \n MASTER DISCRIPTION: {skill[7]} \n \n СOMMENT: {skill[-1]} \n end"

                __Y2 = board.draw_text_block(__temp, (28, 6 + __Ylines), (100, 6 + __Ylines))[2][1]
                board.draw_line((27, 5 + __Ylines), (30 + random.randint(1, 10), 5 + __Ylines), ".")
                board.draw_line((27, 5 + __Ylines), (27, 7 + random.randint(1, 3) + __Ylines), ".")

                while __Y2 > __Y1 + 2:
                    board.draw_point((4, __Y1 + 2), "▒")
                    board.draw_line((5, __Y1 + 2), (23, __Y1 + 2), "░")
                    __Y1 += 1

                board.draw_point((4, __Y1 + 2), "▒")
                board.draw_line((5, __Y1 + 2), (23, __Y1 + 2), "░")
                board.draw_line((4, __Y1 + 3), (24, __Y1 + 3), "▒")
                __Ylines = __Y1 + 3

        return board.get_str()

    def out(self, key=0):
        __out = self.get_head()
        if key > 0:
            __out += self.__get_skills_cards(key)

        self._out_in_file(__out)

    def get_pool(self, key=0):
        __out = self.get_head()
        if key > 0:
            __out += self.__get_skills_cards(key)

        return __out


class Biography(Catalog):
    @property
    def resoursesPath(self):
        return os.fsencode(".resourses/bio/")

    @property
    def inputExeptions(self):
        return ["None"]

    @property
    def inputCategories(self):
        return ["Name", "Age", "Race", "Title",  "Background", "Special"]

    def generate(self, __grade=3):
        return 0

    def get_head(self):
        board = formater.Board()
        self.open()
        board.draw_line((1, 2), (100, 2), "▓")
        __txt = f"NAME: \n •{self.value[0][0]} \n \n TITLE: \n •{self.value[0][3]}"
        __txt += f" \n \n AGE: \n •{self.value[0][1]} \n \n RACE: \n •{self.value[0][2]}"
        __Y1 = board.draw_text_block(__txt, (5, 4), (100, 4))[2][1]
        board.draw_rectangle((1, __Y1 + 2), (100, __Y1 + 2), (100, __Y1 + 4))
        __txt = f"   • {self.value[0][4]} \n \n \n \n    • {self.value[0][5]}"
        __Y1 = board.draw_text_block(__txt, (5, __Y1 + 6), (100, __Y1 + 6))[2][1]
        board.draw_rectangle((1, 2), (4, 2), (4, __Y1 + 1))

        return board.get_str()

    def out(self):
        __out = self.get_head()

        self._out_in_file(__out)

    def get_bio(self):

        __out = self.get_head()

        return __out


class CharList(Primitive):

    def __init__(self, filepath, filename):
        self.item_path = f"{filepath}_{filename }/"
        self.filepath = filepath
        self.filename = filename
        self.value = []
        self.fileId = os.fsencode(filepath + filename)
        self.outId = os.fsencode("output/" + filename+".txt")

        if not os.path.exists(self.fileId):
            inventory = Inventory(self.item_path, filename + "_inventory")
            spell_book = Inventory(self.item_path, "spell_book")
            bio = Biography(self.item_path, f"{filename}_bio")
            bio.input()

        if not os.access(self.fileId, os.F_OK):
            try:
                os.makedirs(os.fsencode(self.filepath))
            except FileExistsError:
                pass

            __tempfile = open(self.fileId, "w")
            __tempfile.write(f"[[],[\"{filename}_inventory\", \"spell_book\"]]")
            __tempfile.close()

        self.value = [[],[]]

    def delite_item(self,__itemName):
        os.remove(self.item_path + __name)

    def create_pool(self, __name):
        self.open()
        new_pool =  Pool(self.item_path, __name)
        self.value[0] += [__name]
        self.save()

    def edit_pool(self, __name):
        pool =  Pool(self.item_path, __name)
        pool.edit()

    def input_pool(self,__name):
        pool =  Pool(self.item_path, __name)
        pool.input()

    def out_pool(self,__name, key):
        pool =  Pool(self.item_path, __name)
        pool.out(key)

    def create_inventory(self, __name):
        self.open()
        inventory =  Inventory(self.item_path, __name)
        self.value[1] += [__name]
        self.save()

    def edit_inventory(self, __name):
        inventory =  Inventory(self.item_path, __name)
        inventory.edit()

    def input_inventory(self,__name):
        inventory =  Inventory(self.item_path, __name)
        inventory.input()

    def out_inventory(self,__name, key):
        inventory =  Inventory(self.item_path, __name)
        inventory.out(key)

    def edit_bio(self):
        bio = Biography(self.item_path, f"{self.filename}_bio")
        bio.edit()

    def out_bio(self):
        bio =  Biography(self.item_path, f"{self.filename}_bio")
        bio.out()

    def out(self, key = 0):
        self.open()
        bio =  Biography(self.item_path, f"{self.filename}_bio")
        __out = bio.get_bio()
        __out += "\n" * 2
        for i in self.value[1]:
            inventory = Inventory(f"{self.filepath}_{self.filename }/", i)
            print(inventory.get_inventory(3))
            print("(!)")
            __out += inventory.get_inventory(key)
        __out += "\n" * 2
        for i in self.value[0]:
            pool =  Pool(f"{self.filepath}_{self.filename }/", i)
            print(pool.get_pool(3))
            __out += pool.get_pool(key)

        self._out_in_file(__out)
