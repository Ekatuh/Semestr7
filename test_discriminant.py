import unittest
import discriminant


class TestDiscriminant(unittest.TestCase):
    def test_positive_discriminant(self):
        # Положительный тест: D > 0
        self.assertEqual(discriminant.discriminant(1, 5, 6), 8)

    def test_zero_discriminant(self):
        # Положительный тест: D = 0
        self.assertEqual(discriminant.discriminant(1, 2, 1), 0)

    def test_negative_discriminant(self):
        # Негативный тест: D < 0
        self.assertEqual(discriminant.discriminant(5, 2, 3), -56)
