import unittest
import timeit

import formater as f





class TestFormater(unittest.TestCase):
    def test_draw_point(self):
        self.assertEqual(
            f.draw_point((1,1)),
            {(1,1,'#')}
        )

    def test_draw_point_with_filler(self):
        self.assertEqual(
            f.draw_point((25,25,"*")),
            {(25,25,'*')}
        )
