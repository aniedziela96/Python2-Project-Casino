from races.mouse import Mouse
from races.track import Track
from races.race import Race
from races.races import Races
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.track1 = Track("rising", 8)
        self.track2 = Track("flat", 6)

        self.mouse11 = Mouse("Standard", 10.25, 0, "flat",
                 1)
        self.mouse12 = Mouse("Minimum", 10, -1, "flat",
                 0)
        self.mouse13 = Mouse("Turbo", 10.5, 1, "rising",
                 1)
        self.mouse14 = Mouse("Turbo2", 10.5, 1, "rising",
                 1.3)
        self.mouse15 = Mouse("Turbo3", 10.5, 1, "rising",
                 2)
        
        self.race1 = Race(self.track1, [self.mouse11, self.mouse12, self.mouse13, self.mouse14
                                       , self.mouse15])
        
        self.race2 = Race(self.track2, [self.mouse11, self.mouse12, self.mouse13, self.mouse14
                                       , self.mouse15])

    def test_start_race(self):
        self.assertEqual(self.race1.start_race()[0],  0.7804878048780488)
        self.assertEqual(self.race1.start_race()[2],  0.6449431240693383)
        self.assertEqual(self.race1.start_race()[0] > self.race1.start_race()[2], True)
        self.assertEqual(self.race1.start_race()[1] == "has not finished the race!", True)
        self.assertEqual(self.race1.start_race()[2] > self.race1.start_race()[3], True)
        self.assertEqual(self.race1.start_race()[3] > self.race1.start_race()[4], True)

    def test_get_winners(self):
        self.assertEqual(self.race2.get_winners(self.race2.start_race()), [4])
        self.assertEqual(self.race1.get_winners(self.race2.start_race()), [4])


if __name__ == "__main__":
    unittest.main()
