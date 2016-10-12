import unittest
from Workout.Processor.src.WorkoutExerciseProcessor import WorkoutExerciseProcessor


class WorkoutExerciseProcessorTest(unittest.TestCase):
    normalSet = ["Test Exercise", "50*12", "50*12", "50*12", "50*12"]
    dropSet = ["Test Exercise", "50*12,30*12", "50*12,30*12", "50*12,30*12", "50*12,30*12"]
    superSet = ["Test Exercise", "50*12&30*12", "50*12&30*12", "50*12&30*12", "50*12&30*12"]
    superDropSet = ["Test Exercise", "50*12,30*12&25*12,12.5*12", "50*12,30*12&25*12,12.5*12",
                    "50*12,30*12&25*12,12.5*12",
                    "50*12,30*12&25*12,12.5*12"]
    repeatedNormal = ["Test Exercise", "50*12", "-", "-", "-"]
    repeatedDropSet = ["Test Exercise", "50*12,30*12", "-", "-", "-"]
    repeatedSuperSet = ["Test Exercise", "50*12&30*12", "-", "-", "-"]
    repeatedSuperDropSet = ["Test Exercise", "50*12,30*12&25*12,12.5*12", "-", "-", "-"]
    repeatedNormalWithTwoStars = ["Test Exercise", "50*12 **4"]
    repeatedDropSetWithTwoStars = ["Test Exercise", "50*12,30*12 **4"]
    repeatedSuperSetWithTwoStars = ["Test Exercise", "50*12&25*12 **4"]
    repeatedSuperDropSetWithTwoStars = ["Test Exercise", "50*12,30*12&25*12,12.5*12 **4"]

    def test_normalSet(self):
        wep = WorkoutExerciseProcessor(self.normalSet)
        self.doTestNormal(wep)

    def doTestNormal(self, wep):
        expectedSets = 4
        expectedWeights = [["50"]]
        expectedReps = [["12"]]

        res = wep.getAllExercises()[0]  # we only have 1 exercise

        sets = res.getSetCount()
        weights = res.getWeights()
        reps = res.getReps()

        self.assertEqual(sets, expectedSets)

        for s in weights:
            self.assertEqual(s, expectedWeights)

        for r in reps:
            self.assertEqual(r, expectedReps)

    def test_dropSet(self):
        wep = WorkoutExerciseProcessor(self.dropSet)
        self.doTestDropSet(wep)

    def doTestDropSet(self, wep):
        expectedSets = 4
        expectedWeights = [["50", "30"]]
        expectedReps = [["12", "12"]]

        res = wep.getAllExercises()[0]  # we only have 1 exercise

        sets = res.getSetCount()
        weights = res.getWeights()
        reps = res.getReps()

        self.assertEqual(sets, expectedSets)

        for s in weights:
            self.assertEqual(s, expectedWeights)

        for r in reps:
            self.assertEqual(r, expectedReps)

    def test_superSet(self):
        wep = WorkoutExerciseProcessor(self.superSet)
        self.doTestSuperSet(wep)

    def doTestSuperSet(self, wep):
        expectedSets = 4
        expectedWeights = [["50"], ["30"]]
        expectedReps = [["12"], ["12"]]

        res = wep.getAllExercises()[0]  # we only have 1 exercise

        sets = res.getSetCount()
        weights = res.getWeights()
        reps = res.getReps()

        self.assertEqual(sets, expectedSets)

        for s in weights:
            self.assertEqual(s, expectedWeights)

        for r in reps:
            self.assertEqual(r, expectedReps)

    def test_superDropSet(self):
        wep = WorkoutExerciseProcessor(self.superDropSet)
        self.doTestSuperDropSet(wep)

    def doTestSuperDropSet(self, wep):
        expectedSets = 4
        expectedWeights = [["50", "30"], ["25", "12.5"]]
        expectedReps = [["12", "12"], ["12", "12"]]

        res = wep.getAllExercises()[0]  # we only have 1 exercise

        sets = res.getSetCount()
        weights = res.getWeights()
        reps = res.getReps()

        self.assertEqual(sets, expectedSets)

        for s in weights:
            self.assertEqual(s, expectedWeights)

        for r in reps:
            self.assertEqual(r, expectedReps)

    def test_repeatedNormal(self):
        wep = WorkoutExerciseProcessor(self.repeatedNormal)
        self.doTestNormal(wep)
        

    def test_repeatedDropSet(self):
        wep = WorkoutExerciseProcessor(self.repeatedDropSet)
        self.doTestDropSet(wep)
        

    def test_repeatedSuperSet(self):
        wep = WorkoutExerciseProcessor(self.repeatedSuperSet)
        self.doTestSuperSet(wep)

    def test_repeatedSuperDropSet(self):
        wep = WorkoutExerciseProcessor(self.repeatedSuperDropSet)
        self.doTestSuperDropSet(wep)        

    def test_repeatedNormalWithTwoStars(self):
        wep = WorkoutExerciseProcessor(self.repeatedNormalWithTwoStars)
        self.doTestNormal(wep)

    def test_repeatedDropSetWithTwoStars(self):
        wep = WorkoutExerciseProcessor(self.repeatedDropSetWithTwoStars)
        self.doTestDropSet(wep)

    def test_repeatedSuperSetWithTwoStars(self):
        wep = WorkoutExerciseProcessor(self.repeatedSuperSetWithTwoStars)
        self.doTestSuperSet(wep)

    def test_repeatedSuperDropSetWithTwoStars(self):
        wep = WorkoutExerciseProcessor(self.repeatedSuperDropSetWithTwoStars)
        self.doTestSuperDropSet(wep)


# Code so that tests can be run as individual files
if __name__ == '__main__':
    unittest.main()
