from Workout.Loader.src.Loader import Loader
from Workout.Data.src.Workout.Workout import Workout
from Workout.Data.src.Exercise.Exercise import Exercise


class Processor(object):
    """
    Process the loaded file string into a Workout
    """
    __fr = None
    __contents = None
    __lastWorkout = None

    def __init__(self, filename=None):
        if filename is None:
            raise Exception("Must provide filename")

        self.__fr = Loader(filename)

    def readFile(self, force=False):
        """
        READS the file into the program, if NO file has been loaded yet
        :return: A string containing all of the data from the file
        """
        if self.__contents is None or force is True:  # load the file if it hasnt been loaded yet
            try:
                self.__contents = self.__fr.read()
            except IOError, e:
                raise IOError(e)

    def clearMemory(self):
        """
        Removes the information from the contents string
        """
        self.__contents = ""

    def process(self):
        """
        :return: A list of Workout objects containing all of the workouts in the file
        """
        print "Starting processing"

        self.readFile()

        if len(self.__contents) < 1:
            raise Exception("File is empty")

        self.__contents = self.__contents.splitlines()

        return self.__createWorkout(self.__contents)

    def __createWorkout(self, fileContents):
        titleAndDate = fileContents[0]

        workout = self.__createWorkoutAndProcessTitleAndDate(titleAndDate)

        workoutExercises = self.__processExercises(fileContents[1:])

        workout.addAllExercises(workoutExercises)
        return workout

    def __createWorkoutAndProcessTitleAndDate(self, title):

        dateAndTitle = title.split("@")
        date = dateAndTitle[0]
        title = dateAndTitle[1]

        workout = Workout(title)

        workout.setDate(self.__stripDate(date))

        return workout

    def __stripDate(self, date):
        """
        Strip the !(...) characters and get only the 10 character date
        :param date:
        :return:
        """
        startIndexOfDate = 0
        endIndexOfDate = 10
        return date.translate(None, "!()")[startIndexOfDate:endIndexOfDate]

    def __processExercises(self, exercises):
        # get number of sets and hand information
        exerciseContainer = []

        while len(exercises) > 0:
            name, sets, hands, weightMultiplier = self.__extractNameSetsHandMultiplier(exercises[0])
            sets = int(sets)
            # remove name from list
            del exercises[0]

            # set exercise information
            newExercise = Exercise(name)
            newExercise.setSets(sets)
            newExercise.setHands(hands)
            newExercise.setWeightMultiplier(weightMultiplier)

            # loop through X number of sets and process the exercises
            weights, reps = self.__processExerciseSetsString(exercises[:sets])

            # remove the sets from the list
            del exercises[:sets]

            newExercise.setWeights(weights)
            newExercise.setReps(reps)

            exerciseContainer.append(newExercise)

        return exerciseContainer

    def __extractNameSetsHandMultiplier(self, param):
        nameAndSets = param.split(";")
        name = nameAndSets[0]
        sets = nameAndSets[1]

        setsAndHand = sets.split("/")

        # re-assign to hold correct value for sets
        sets = setsAndHand[0]
        hand = setsAndHand[1]

        if len(setsAndHand) < 3:  # use default multiplier for weight
            setsAndHand.append("*1")

        weightMultiplier = setsAndHand[2]

        return name, sets, hand, weightMultiplier

    def __processExerciseSetsString(self, exercises):
        # split for supersets, do nothing if not superset
        exercises = [x.split("&") for x in exercises]

        weights = []
        reps = []
        for sets in exercises:
            weightsForSet = []
            repsForSet = []
            for set in sets:
                w, rep = self.__processSet(set)
                weightsForSet.append(w)
                repsForSet.append(rep)

            weights.append(weightsForSet)
            reps.append(repsForSet)

        return weights, reps

    def __processSet(self, set):
        weights, reps = [], []

        if "," in set:
            # handle dropset/s
            dropsets = set.split(",")

            for drop in dropsets:
                w, rep = self.__processWeightsAndReps(drop)
                weights.append(w)
                reps.append(rep)
        else:
            # handle normal
            w, rep = self.__processWeightsAndReps(set)
            weights.append(w)
            reps.append(rep)

        return weights, reps

    def __processWeightsAndReps(self, drop):
        w = drop.split("x")
        return w[0], w[1]


r = Processor("../../TestData/ShoulderWorkout.txt")
print r.process()
