
import unittest
from planet_info import query_planets

class TestPlanetQueries(unittest.TestCase):

    def test_query_mass(self):
        result = query_planets("How massive is Earth?")
        self.assertIn("mass", result)

    def test_query_distance(self):
        result = query_planets("What is the distance of Saturn from the Sun?")
        self.assertIn("distance_from_sun", result)

    def test_query_moons(self):
        result = query_planets("What moons does Saturn have?")
        self.assertIn("moons", result)

    def test_query_everything(self):
        result = query_planets("Tell me everything about Saturn")
        self.assertIn("mass", result)
        self.assertIn("distance_from_sun", result)
        self.assertIn("moons", result)

    def test_query_pluto(self):
        result = query_planets("Is Pluto in the list of planets?")
        self.assertEqual(result, "Pluto is not in the list of planets.")

    def test_invalid_query(self):
        result = query_planets("Tell me about Vulcan")
        self.assertEqual(result, "planet not found")

if __name__ == '__main__':
    unittest.main()
