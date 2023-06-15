import unittest
from board import Board


class Test(unittest.TestCase):
    def setUp(self):
        self.b1 = Board([[1, 2, 3, 4, 5], [16, 17, 18, 19, 20], [31, 32, '\N{BLACK CIRCLE}', 33, 34],
        [46, 47, 48, 49, 50], [61, 62, 63, 66, 65]])
        self.b2 = Board([['\N{BLACK CIRCLE}', 2, 3, 4, 5], [16, 17, 18, 19, 20], [31, 32, '\N{BLACK CIRCLE}', 33, 34],
        [46, 47, 48, 49, 50], [61, 62, 63, 66, 65]])
        self.b3 = Board([[1, 2, 3, 4, 5], [16, 17, 18, 19, 20], [31, 32, '\N{BLACK CIRCLE}', 33, 34],
        [46, 47, 48, 49, 50], [61, 62, 63, 66, 65]])
        self.b4 = Board([[1, 2, 3, 4, 5], [16, 17, 18, 19, 20], [31, 32, '\N{BLACK CIRCLE}', 33, 34],
        [46, 47, 48, 49, 50], [61, 62, 63, 66, 65]])
        self.b5 = Board([[1, 2, 3, 4, 5], [16, 17, 18, 19, 20], 
                         ['\N{BLACK CIRCLE}', '\N{BLACK CIRCLE}', '\N{BLACK CIRCLE}', '\N{BLACK CIRCLE}', '\N{BLACK CIRCLE}'],
                        [46, 47, 48, 49, 50], [61, 62, 63, 66, 65]])
        self.b6 = Board([[1, 2, '\N{BLACK CIRCLE}', 4, 5], [16, 17, '\N{BLACK CIRCLE}', 19, 20], 
                         [31, 32, '\N{BLACK CIRCLE}', 33, 34],
                        [46, 47, '\N{BLACK CIRCLE}', 49, 50], [61, 62, '\N{BLACK CIRCLE}', 66, 65]])
        self.b7 = Board([['\N{BLACK CIRCLE}', 2, 3, 4, 5], [16, '\N{BLACK CIRCLE}', 18, 19, 20], 
                         [31, 32, '\N{BLACK CIRCLE}', 33, 34],
                        [46, 47, 48, '\N{BLACK CIRCLE}', 50], [61, 62, 63, 66, '\N{BLACK CIRCLE}']])

    def test_check(self):
        self.b1.check(1)
        self.b3.check(12)
        self.assertEqual(self.b1.columns, self.b2.columns)
        self.assertEqual(self.b3.columns, self.b4.columns)

    def test_is_bingo(self):
        self.assertEqual(self.b5.is_bingo(), True)
        self.assertEqual(self.b6.is_bingo(), True)
        self.assertEqual(self.b7.is_bingo(), True)
        self.assertEqual(self.b3.is_bingo(), False)



if __name__ == "__main__":
    unittest.main()

