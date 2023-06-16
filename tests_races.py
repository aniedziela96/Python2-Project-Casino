from races.mouse import Mouse
from races.track import Track
from races.race import Race
from races.races import Races
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.track1 = Track("rising", 15)
        self.track2 = Track("flat", 12)

        self.mouse11 = Mouse("Standard", 4.2, 4.75, "sloping",
                 1)
        self.mouse12 = Mouse("Minimum", 3.5, 4.5, "flat",
                 0)
        self.mouse13 = Mouse("Turbo", 4.75, 5, "rising",
                 1)
        self.mouse14 = Mouse("Turbo2", 4.75, 5, "rising",
                 1.3)
        self.mouse15 = Mouse("Turbo3", 4.75, 5, "rising",
                 2)
        
        self.race1 = Race(self.track1, [self.mouse11, self.mouse12, self.mouse13, self.mouse14
                                       , self.mouse15])
        
        self.race2 = Race(self.track2, [self.mouse11, self.mouse12, self.mouse13, self.mouse14
                                       , self.mouse15])

    def test_start_race(self):
        # standard mouse
        self.assertEqual(self.race1.start_race()[0],  1.3672208261659407)
        # mouse with this preference
        self.assertEqual(self.race1.start_race()[2],  1.3256442347260304)
        # standard mouse, flat track
        self.assertEqual(self.race2.start_race()[0],  1.1892970706058092)
        # very bad daily well-being
        self.assertEqual(self.race1.start_race()[1] == "has not finished the race!", True)
        # times comparision
        self.assertEqual(self.race1.start_race()[0] > self.race1.start_race()[2], True)
        self.assertEqual(self.race1.start_race()[2] > self.race1.start_race()[3], True)
        self.assertEqual(self.race1.start_race()[3] > self.race1.start_race()[4], True)
        
    def test_get_winners(self):
        # winner check
        self.assertEqual(self.race2.get_winners(self.race2.start_race()), [4])
        self.assertEqual(self.race1.get_winners(self.race2.start_race()), [4])


if __name__ == "__main__":
    unittest.main()
