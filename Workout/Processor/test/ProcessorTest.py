import unittest
from Workout.Processor.src.Processor import Processor
from Workout.Loader.src.Loader import Loader

class ProcessorTest(unittest.TestCase):
    testDataPath = "D:\Documents\Projects\PythonWorkoutManager\TestData\LegWorkout.txt"
    fr = Loader(testDataPath)
    r = Processor(fr.read())
    workout = r.process()

    def test_workoutName(self):
        name = self.workout.getName()
        expectedName = "Legs"

        self.assertEquals(name, expectedName)

    def test_exerciseOneSet(self):
        expectedSets = 1
        expectedName = "Front Squat"
        expectedWeights = [[['50']]]
        expectedReps = [[['8']]]

        # this will return the exercise with 1 set

        ex = self.workout.getExerciseAt(1)

        name, sets, weights, reps = self.__getExerciseInfo(ex)
        self.__checkEqualOutputs(name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps)
        

    def test_oneExerciseWithRepeats(self):
        expectedSets = 5
        expectedName = "Squats"
        expectedWeights = [[['50']],[['50']],[['50']],[['50']],[['60']]]
        expectedReps = [[['8']],[['8']],[['8']],[['8']],[['8']]]

        ex = self.workout.getExerciseAt(0)
        name, sets, weights, reps = self.__getExerciseInfo(ex)

        self.__checkEqualOutputs(name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps)

    def test_superDropSets(self):
        expectedSets = 4
        expectedName = "Leg ext & Leg curls"

        # ain't that pretty
        expectedWeights = [
            [['45'],['45']], 
            [['50', '25'],['50']], 
            [['55'],['55','45']],
            [['50','25'],['40','30']]
            ] 
        expectedReps = [
            [['12'],['12']], 
            [['12','10'],['12']],
            [['12'],['8','12']],
            [['15','10'],['15','15']]
            ]

        ex = self.workout.getExerciseAt(2)
        name, sets, weights, reps = self.__getExerciseInfo(ex)

        self.__checkEqualOutputs(name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps)

    def test_underscoreForBodyweightWithRepeats(self):
        expectedSets = 4
        expectedName = "Calf Raises & Good Morning"
        expectedWeights = [
            [['_'],['20']],
            [['_'],['20']],
            [['_'],['20']],
            [['_']]
        ]

        expectedReps = [
            [['50'],['15']],
            [['50'],['15']],
            [['30'],['15']],
            [['30']]
        ]

        ex = self.workout.getExerciseAt(3)
        name, sets, weights, reps = self.__getExerciseInfo(ex)
        self.__checkEqualOutputs(name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps)

    def test_exerciseNameAppendedSets(self):
        expectedName = "Imaginary Squat"
        expectedSets = 4
        expectedWeights = [
            [['30']],
            [['30']],
            [['30']],
            [['30']]
        ]
        expectedReps = [
            [['4']],
            [['4']],
            [['4']],
            [['4']]
        ]

        ex = self.workout.getExerciseAt(4) # get imaginary squat
        name, sets, weights, reps = self.__getExerciseInfo(ex)
        self.__checkEqualOutputs(name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps)


    def test_exerciseNameAppendedSetsAndHands(self):
        expectedName = "Imaginary Squat"
        expectedSets = 5
        expectedWeights = [
            [['30']],
            [['30']],
            [['30']],
            [['30']],
            [['30']]
        ]
        expectedReps = [
            [['4']],
            [['4']],
            [['4']],
            [['4']],
            [['4']]
        ]
        expectedHands = '1' # default is 2 so test with 1

        ex = self.workout.getExerciseAt(5) # get imaginary squat
        name, sets, weights, reps = self.__getExerciseInfo(ex)
        self.__checkEqualOutputs(name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps)

        hands = ex.getHands()

        self.assertEqual(expectedHands, hands)


    def test_exerciseNameAppendedSetsAndHandsAndWeightMultiplier(self):
        expectedName = "Imaginary Squat"
        expectedSets = 6
        expectedWeights = [
            [['30']],
            [['30']],
            [['30']],
            [['30']],
            [['30']],
            [['30']]
        ]
        expectedReps = [
            [['4']],
            [['4']],
            [['4']],
            [['4']],
            [['4']],
            [['4']]
        ]
        expectedHands = '1' # default is 2 so test with 1
        expectedWeightMultipler = '*2'

        ex = self.workout.getExerciseAt(6) # get imaginary squat
        name, sets, weights, reps = self.__getExerciseInfo(ex)
        self.__checkEqualOutputs(name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps)

        hands = ex.getHands()
        self.assertEqual(expectedHands, hands)

        weightMult = ex.getWeightMultiplier()
        self.assertEqual(expectedWeightMultipler, weightMult)

    """
    HELPER METHODS BELOW
    """
    
    def __checkEqualOutputs(self, name, sets, weights, reps, expectedName, expectedSets, expectedWeights, expectedReps):
        self.assertEquals(name, expectedName)
        self.assertEquals(sets, expectedSets)

        for i in range(len(expectedWeights)):
            self.assertEquals(weights[i], expectedWeights[i])

        for i in range(len(expectedReps)):
            self.assertEquals(reps[i], expectedReps[i])
            

    def __getExerciseInfo(self, ex):
        return ex.getName(),ex.getSetCount(),ex.getWeights(),ex.getReps()


# Code so that tests can be run as individual files
if __name__ == '__main__':
    unittest.main()