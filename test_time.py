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
a = f.grid_to_str(grid)
"""

testing_comp2 = """
import formater_old as f_old
board = f_old.Board()
board.draw_point((5,5))
board.draw_point((20,20))
board.draw_point((99,1000))
a = board.get_str()
"""

print()

elapsed_time = timeit.timeit(testing_code1, number=10000)
print("[points] new runtime:", elapsed_time)

elapsed_time = timeit.timeit(testing_code_old1, number=10000)
print("[points] old runtime:", elapsed_time)

elapsed_time = timeit.timeit(testing_comp1, number=10000)
print("[compilation] new runtime:", elapsed_time)

elapsed_time = timeit.timeit(testing_comp2, number=10000)
print("[compilation] old runtime:", elapsed_time)


print()
