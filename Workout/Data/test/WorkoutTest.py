from unittest import TestCase
from Workout.Data.src.Exercise.Exercise import Exercise
from Workout.Data.src.Workout.Workout import Workout


class WorkoutTest(TestCase):
    w = None
    ex1 = Exercise("test1",
                  {'name': "Bench Press", 'sets': 4,
                   'weight': [50, 60, 70, 80],
                   'reps': [12, 10, 8, 6]})
    ex2 = Exercise("test2",
                  {'name': "Shoulder Press", 'sets': 4,
                   'weight': [50, 60, 70, 80],
                   'reps': [12, 10, 8, 6]})

    def setUp(self):
        if self.w is None or len(self.w.count()) < 1:
            self.w = Workout("Test")
            self.w.addExercise(self.ex2)
            self.w.addExercise(self.ex1)

    def tearDown(self):
        self.w.clear()

    def test_getexercise(self):
        exercise = self.w.getExercise("Bench Press")

        self.assertEquals(exercise.getName(), self.ex1.getName())

    def test_getexerciseat(self):
        exercise = self.w.getExerciseAt(0)

        self.assertEquals(exercise.getName(), self.ex2.getName())

    def test_getallexercises(self):
        exercise = self.w.getAllExercises()

        self.assertEquals(exercise[0].getName(), self.ex2.getName())

    def test_removeexercise(self):
        self.w.removeExercise("Bench Press")

        self.assertEqual(self.w.count(), 1)

    def test_removeexerciseat(self):
        self.w.removeExerciseAt(0)

        self.assertEqual(self.w.count(), 1)
