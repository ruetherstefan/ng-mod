import unittest

from src.baustein.Baustein import Baustein


class BausteinTest(unittest.TestCase):

    def test_get_position__0_0(self):

        undertest = Baustein()
        undertest.set_position_index([0, 0])

        self.assertEqual(undertest.get_position(), [0, 0])

    def test_get_position__5_3(self):

        undertest = Baustein()
        undertest.set_position_index([5, 3])

        self.assertEqual(undertest.get_position(), [5 * 32, 3 * 32])

    def test_get_position__NotInitialized(self):

        undertest = Baustein()

        with self.assertRaises(TypeError):
            self.assertEqual(undertest.get_position(), [0, 0])
