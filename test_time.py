import timeit


testing_code1 ="""
import formater as f
grid = f.draw_point((5,5))
grid = f.draw_point((20,20), grid)
grid = f.draw_point((99,1000), grid)
"""
testing_code_old1 ="""
import formater_old as f_old
board = f_old.Board()
board.draw_point((5,5))
board.draw_point((20,20))
board.draw_point((99,1000))
"""

testing_comp1 = """
import formater as f
grid = f.draw_point((5,5))
grid = f.draw_point((20,20), grid)
grid = f.draw_point((99,1000), grid)
a = f.assembly(grid)
"""

testing_comp2 = """
import formater_old as f_old
board = f_old.Board()
board.draw_point((5,5))
board.draw_point((20,20))
board.draw_point((99,1000))
a = board.get_str()
"""

tc_tuple = """
gridt={(a,a,"#") for a in range(0,10000)}

a = gridt.copy()
if (1111,1111,'#'):
    a = 1+1
"""
tc_dict = """
gridd = {(a,a):"#" for a in range(0,10000)}

a = gridd.copy()
if (1111,1111,'#'):
    a = 1+1
"""

tc_line1 = """
import formater as f
grid = f.draw_line((5,5), (100,4000))
grid = f.draw_line((20,20), (1,3000), grid)
grid = f.draw_line((99,1000), (10,4500), grid)
"""

tc_line2 = """
import formater_old as f_old
board = f_old.Board()
board.draw_line((5,5), (100,4000))
board.draw_line((20,20), (1, 3000))
board.draw_line((99,1000), (19,4500))
"""


print()

# elapsed_time = timeit.timeit(testing_code1, number=10000)
# print("[points] new runtime:", elapsed_time)
#
# elapsed_time = timeit.timeit(testing_code_old1, number=10000)
# print("[points] old runtime:", elapsed_time)
#
# elapsed_time = timeit.timeit(testing_comp1, number=10000)
# print("[compilation] new runtime:", elapsed_time)
#
# elapsed_time = timeit.timeit(testing_comp2, number=10000)
# print("[compilation] old runtime:", elapsed_time)
#
# elapsed_time = timeit.timeit(tc_tuple, number=10000)
# print("[grid type] tuple:", elapsed_time)
#
# elapsed_time = timeit.timeit(tc_dict, number=10000)
# print("[grid type] dict:", elapsed_time)

elapsed_time = timeit.timeit(tc_line1, number=5000)
print("[lines] new runtime:", elapsed_time)

elapsed_time = timeit.timeit(tc_line2, number=5000)
print("[lines] old runtime:", elapsed_time)

print()
