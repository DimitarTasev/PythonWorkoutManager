import unittest
from Workout.Data.src.Exercise import Exercise
from Workout.Data.src.Workout import Workout


class WorkoutTest(unittest.TestCase):
    workout = None
    ex1 = Exercise("Bench Press", 4,
                   [50, 60, 70, 80], [12, 10, 8, 6])
    ex2 = Exercise("Shoulder Press", 4,
                   [50, 60, 70, 80], [12, 10, 8, 6])

    def setUp(self):
        if self.workout is None or len(self.workout.count()) < 1:
            self.workout = Workout("Test")
            self.workout.addExercise(self.ex2)
            self.workout.addExercise(self.ex1)

    def tearDown(self):
        self.workout.clear()

    def test_getexercise(self):
        exercise = self.workout.getExercise("Bench Press")

        self.assertEquals(exercise.getName(), self.ex1.getName())
        
    def test_getexerciseat(self):
        exercise = self.workout.getExerciseAt(0)

        self.assertEquals(exercise.getName(), self.ex2.getName())

    def test_getallexercises(self):
        exercise = self.workout.getAllExercises()

        self.assertEquals(exercise[0].getName(), self.ex2.getName())

    def test_removeexercise(self):
        self.workout.removeExercise("Bench Press")

        self.assertEqual(self.workout.count(), 1)

    def test_removeexerciseat(self):
        self.workout.removeExerciseAt(0)

        self.assertEqual(self.workout.count(), 1)

# Code so that tests can be run as individual files
if __name__ == '__main__':
    unittest.main()