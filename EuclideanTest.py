import unittest
from Euclidean import euclidean

class EuclideanTest(unittest.TestCase):

    def test_simple(self):
        rhythm = euclidean(8, 4, 0)
        self.assertEqual(rhythm, [1, 0, 1, 0, 1, 0, 1, 0])


if __name__ == "__main__":
    unittest.main()
