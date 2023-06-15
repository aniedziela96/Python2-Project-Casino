from races.mouse import Mouse
from races.track import Track
from races.race import Race
from races.races import Races
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.track1 = Track("rising", 8)
        self.track2 = Track("flat", 6)
        self.track2 = Track("sloping", 5)
        self.mouse1 = Mouse("Standard", "1", "1", "flat",
                 "1")
        self.mouse2 = Mouse("Minimum", "1", "1", "flat",
                 "1")


if __name__ == "__main__":
    unittest.main()
