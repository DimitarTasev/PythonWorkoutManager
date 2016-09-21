import unittest
from Workout.Loader.src.Loader import Loader


class LoaderTest(unittest.TestCase):
    def test_load(self):
        result = "hi\nthis\nis\ntext\nfile"
        loader = Loader("./TestData/LoaderTestData.txt")
        self.assertEqual(loader.read(), result)
