# TODO this class will have the exercise processing bits from the processor
from Workout.Data.src.Exercise.Exercise import Exercise


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
        for sets in exercises:  # supersets represented as [[set1], [set2]]
            weightsForSet = []
            repsForSet = []

            markedForRepeatWithStarStar = False
            repeatTimes = 0
            
            # check if set is repeated with **n
            if self.__isRepeatedWithStarStar(sets):
                # do what?
                markedForRepeatWithStarStar = True
                repeatTimes = self.__extractRepeatNumber(sets)

            # if repeated, just append last result and that's it
            if self.__isSetRepeatedWithDash(sets):
                w, rep = self.__retrieveCache()
                weights.append(w)
                reps.append(rep)
            else:  # else process the sets properly
                for currentSet in sets:  # processes a single part of a set, i.e. set1 or set2
                    w, rep = self.__processSet(currentSet)
                    weightsForSet.append(w)
                    repsForSet.append(rep)

                if markedForRepeatWithStarStar:
                    # do next thing repeatTimes times
                    for x in range(repeatTimes - 1):
                        w, rep = self.__retrieveCache()
                        weights.append(w)
                        reps.append(rep)
                    
                # fast cache for next set
                self.__cache(weightsForSet, repsForSet)
                # append processed weights and set
                weights.append(weightsForSet)
                reps.append(repsForSet)

        return weights, reps

    def __isRepeatedWithStarStar(self, setString):

        # TODO make this pretties cos it makes me feel sick on the inside
        lastPos = len(setString) - 1
        setString = setString[lastPos].split(" ")
        hasStarStar = False
        for s in setString:
            hasStarStar = True
            break
        return hasStarStar
        
    def __extractRepeatNumber(self, setString):
        """
        This method processes sets with the format
        "set **n"
        "set,set **n"
        "set&set **n"
        "set,set&set,set **4"

        :return: Number of times the set needs to be added to the weights/reps list, which is number of times repeated - 1
        """
        # possible cases here are 
        #["34*34,34*34&34*34,34*34 **4"]

        print "Before split", setString
        setString = setString.split(" ")
        for s in setString:
            if "**" in s:
                return int(s[-1:])


    def __isSetRepeatedWithDash(self, setString):
        return True if setString[0] == '-' else False

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

    def getAllExercises(self):
        return self.m_exercisesContainer
