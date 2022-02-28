import unittest
import timeit

import formater as f

class TestFormater(unittest.TestCase):
    def test_draw_point(self):
        self.assertEqual(
            f.draw_point((1,1)),
            {(1,1):"#"}
        )

    def test_draw_point_with_filler(self):
        self.assertEqual(
            f.draw_point((25,25,"*")),
            {(25,25,):'*'}
        )

    def test_char_input_insted_coordinate_draw_point(self):
        with self.assertRaises(ValueError):
            f.draw_point(("sd", 12, "у"))

    def test_incorrect_filler_draw_point(self):
        with self.assertRaises(ValueError):
            f.draw_point((12, 12, "уqwe"))
            f.draw_point((12, 12, 1))

    def test_draw_line(self):
        self.assertEqual(
        f.draw_line((1,1), (5,1)),
        {(1, 1): '#', (2, 1): '#', (3, 1): '#', (4, 1): '#', (5, 1): '#', }
        )
        self.assertEqual(
        f.draw_line((1,1), (1,1)),
        {(1, 1): '#'}
        )
        self.assertEqual(
        f.draw_line((5,1), (1,3)),
        {(5, 1): '#', (3, 2): '#', (4, 2): '#', (2, 2): '#', (1, 3): '#'}
        )
        self.assertEqual(
        f.draw_line((1,1), (5,2)),
        {(1, 1): '#', (2, 1): '#', (3, 2): '#', (4, 2): '#', (5, 2): '#'}
        )
        self.assertEqual(
        f.draw_line((10,10), (1,10)),
        {(10, 10): '#', (9, 10): '#',
        (8, 10): '#', (7, 10): '#',
        (6, 10): '#', (5, 10): '#',
        (4, 10): '#', (3, 10): '#',
        (2, 10): '#', (1, 10): '#'}
        )
        self.assertEqual(
        f.draw_line((10,10), (10,1)),
        {(10, 10): '#', (10, 9): '#',
        (10, 8): '#', (10, 7): '#',
        (10, 6): '#', (10, 5): '#',
        (10, 4): '#', (10, 3): '#',
        (10, 2): '#', (10, 1): '#'}
        )
