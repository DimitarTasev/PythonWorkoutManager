# TODO this class will have the exercise processing bits from the processor
from Workout.Data.src.Exercise import Exercise
from Workout.Processor.src.WorkoutSetProcessor import WorkoutSetProcessor


class WorkoutExerciseProcessor(object):
    m_exercises = None
    m_exercisesContainer = None

    def __init__(self, exercises=None):
        if exercises is not None:
            self.m_exercises = exercises

        self.m_exercisesContainer = self.__processExercises(self.m_exercises)

    def __processExercises(self, exercises):
        # get number of sets and hand information
        exerciseContainer = []
        setProcessor = WorkoutSetProcessor()

        while len(exercises) > 0:
            name, sets, hands, weightMultiplier = self.__extractNameSetsHandMultiplier(exercises[0], exercises[1:])
            sets = int(sets)
            # remove name from list
            del exercises[0]

            # set exercise information
            newExercise = Exercise(name)
            newExercise.setSets(sets)
            newExercise.setHands(hands)
            newExercise.setWeightMultiplier(weightMultiplier)

            # loop through X number of sets and process the exercises
            weights, reps = setProcessor.process(exercises[:sets])

            # remove the sets from the list
            del exercises[:sets]

            newExercise.setSets(len(weights))  # update with the correct number of sets
            newExercise.setWeights(weights)
            newExercise.setReps(reps)

            exerciseContainer.append(newExercise)

        return exerciseContainer

    def __extractNameSetsHandMultiplier(self, title, exercises):
        if ";" in title:  # title contains information about number of sets
            nameAndSets = title.split(";")
        else:
            nameAndSets = [title]

        name = nameAndSets[0]
        hand = '2'
        weightMultiplier = '*1'

        # if set info is available -> the ;5/1/1 then use that, otherwise count manually
        sets = nameAndSets[1] if len(nameAndSets) > 1 else self.__countAndCreateSetsString(exercises)
        setsAndHand = sets.split("/")
        # re-assign to hold correct value for sets
        sets = setsAndHand[0]

        # TODO could potentially merge the functionality of this and __countAndCreateSetsString()
        if len(setsAndHand) > 1:  # use the provided for hands
            hand = setsAndHand[1]

        if len(setsAndHand) > 2:  # use the provided multiplier for weight
            weightMultiplier = setsAndHand[2]

        return name, sets, hand, weightMultiplier

    def __countAndCreateSetsString(self, exercises):
        lineCounter = 0
        # increment if line doesnt start with letter
        for line in exercises:
            if len(exercises) > 0 and not line[0].isalpha() or line[0] == '_':
                # char is not a letter, therefore it's a set
                lineCounter += 1
            else:  # if line starts with letter,
                break

                # return after exiting the for loop counter
        return "{0}/2/*1".format(str(lineCounter))  # use default values for hands/weight multiplier

    def getAllExercises(self):
        return self.m_exercisesContainer
