import unittest
from Euclidean import euclidean

class EuclideanTest(unittest.TestCase):
    def test_simple(self):
        rhythm = euclidean(8, 4, 0)
        self.assertEqual(rhythm, [1, 0, 1, 0, 1, 0, 1, 0])

        rhythm = euclidean(13, 5, 0)
        self.assertEqual(rhythm, [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0])

        rhythm = euclidean(13, 5, 2)
        self.assertEqual(rhythm, [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])

        # If more pulses than steps, all 1s
        rhythm = euclidean(4, 8, 0)
        self.assertEqual(rhythm, [1, 1, 1, 1])

        rhythm = euclidean(4.3, 8.9, 0.99)
        self.assertEqual(rhythm, [1, 1, 1, 1])

        rhythm = euclidean('4', '2', '0')
        self.assertEqual(rhythm, [1, 0, 1, 0])

if __name__ == "__main__":
    unittest.main()
