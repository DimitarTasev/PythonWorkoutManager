from Workout.Loader.src.Loader import Loader
from Workout.Data.src.Workout.Workout import Workout
from Workout.Data.src.Exercise.Exercise import Exercise


class Processor(object):
    """
    Process the loaded file string into a Workout
    """
    __fileContents = None
    __lastWorkout = None

    def __init__(self, filecontents=None):
        if filecontents is not None:
            self.__fileContents = filecontents

    def setWorkoutText(self, workoutText):
        self.__fileContents = workoutText

    def clearMemory(self):
        """
        Removes the information from the contents string
        """
        self.__fileContents = ""

    def process(self):
        """
        :return: A list of Workout objects containing all of the workouts in the file
        """
        print "Starting processing"

        if len(self.__fileContents) < 1:
            raise Exception("No workout provided in file. Please set one in constructor or using \
            setWorkoutText()")

        self.__fileContents = self.__fileContents.splitlines()

        self.__lastWorkout = self.__createWorkout(self.__fileContents)

        return self.__lastWorkout

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
            weights, reps = self.__processExerciseSetsString(exercises[:sets])

            # remove the sets from the list
            del exercises[:sets]

            newExercise.setWeights(weights)
            newExercise.setReps(reps)

            exerciseContainer.append(newExercise)

        return exerciseContainer

    def __extractNameSetsHandMultiplier(self, title, exercises):
        nameAndSets = title.split(";")
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
            

    def __processExerciseSetsString(self, exercises):
        """
        Receives the exercise string, at this point would be
        [30*5&15*5] and splits it further sets, so it would
        become [[30*5][15*5]], signifying 1 set with a superset

        @param exercises::List of string to be processed and split
        @return The weights and reps from the string passed in the parameter
        """
        # split for supersets, does nothing if not superset
        exercises = [x.split("&") for x in exercises]

        weights = []
        reps = []
        for sets in exercises: # supersets represented as [[set1], [set2]]
            weightsForSet = []
            repsForSet = []

            # if repeated, just append last result and that's it
            if self.__isSetRepeated(sets):
                w, rep = self.__retrieveCache()
                weights.append(w)
                reps.append(rep)
            else: # else process the sets properly
                for currentSet in sets: # processes a single part of a set, i.e. set1 or set2
                    w, rep = self.__processSet(currentSet)
                    weightsForSet.append(w)
                    repsForSet.append(rep)

                # fast cache for next set
                self.__cache(weightsForSet, repsForSet)
                # append processed weights and set
                weights.append(weightsForSet)
                reps.append(repsForSet)

        return weights, reps

    def __isSetRepeated(self, set):
        return True if set[0] == '-' else False

    # Method related global variables, used for caching the previous entries
    __lastWeights, __lastReps = [], []
    def __cache(self, weights, reps):
        self.__lastWeights = weights
        self.__lastReps = reps

    def __retrieveCache(self):
        return self.__lastWeights, self.__lastReps

    def __processSet(self, set):
        """
        Processes a single set (i.e. from input 30*5&15*5, method here should be used to process
        30*5 first and then 15*5 in a consecutive call)
        """
        weights, reps = [], []

        if "," in set:
            # handle dropset/s
            dropsets = set.split(",")

            # dropset is simply split from [dropset1,dropset2] to
            # [[dropset1],[dropset2]] so it can be processed with the same method
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

    def __processWeightsAndReps(self, setInfo):
        """
        Processes the input in a form of 30*5 or 30x5 (different syntax for the same thing)
        @return weight, reps as individual members, must be received as 
        a, b = __processWeightsAndReps
        """
        delimiterChar = '*' if '*' in setInfo else 'x'

        w = setInfo.split(delimiterChar)
        return w[0], w[1]
