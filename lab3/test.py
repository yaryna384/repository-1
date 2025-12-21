import unittest
from app import Figure

class TestFigure(unittest.TestCase):
    def setUp(self):
        self.obj = Figure("квадрат", 10)

    def test_figure_type(self):
        self.assertEqual(self.obj.get_figure_type(), "квадрат", "Тип має бути квадрат")

    def test_figure_lengh(self):
        self.assertEqual(self.obj.get_figure_length(), 10, "Довжина має бути 10")

    def test_obj(self):
        self.assertIsInstance(self.obj, Figure)

    def test_get_angles(self):
        fig = "трикутник"
        triangle = Figure(fig, 1)
        self.assertEqual(triangle.get_angles, 3, f"У {fig} має бути 3 кути!")

if __name__ == '__main__':
    unittest.main()