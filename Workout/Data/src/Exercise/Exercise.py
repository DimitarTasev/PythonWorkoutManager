class Exercise(object):
    __name = ""
    __sets = 0
    __weights = []
    __reps = []
    __hands = -1
    __weightMultiplier = 1
    __superset = False

    def __init__(self, name=None):
        if name is None:
            self.__name = "NotSet"
        else:
            self.__name = name

        if "&" in self.__name:
            self.__superset = True

    def __str__(self):
        return "\nName: " + str(self.__name) + " Sets: " + str(self.__sets) + "\n" + "Weights: " + str(
            self.__weights) + "\n" + "Reps: " + str(self.__reps)

    def getName(self):
        """
        :return: String: Returns the exercise name as a string

        """
        return self.__name

    def getSets(self):
        """
        @return the number of sets in the exercise
        """
        return self.__sets

    def setSets(self, sets, initialiseContainers=True):
        self.__sets = int(sets)
        if initialiseContainers:
            self.__initialiseWeights(self.__sets)
            self.__initialiseReps(self.__sets)

    def __initialiseReps(self, setCount):
        if len(self.__reps) < setCount:
            for i in range(setCount):
                self.__reps.append(0)

    def __initialiseWeights(self, setCount):
        if len(self.__weights) < setCount:
            for i in xrange(setCount):
                self.__weights.append(0)

    def setWeights(self, weights):
        self.__weights = weights

    def getWeights(self):
        return self.__weights

    def setWeightForSet(self, setNum, weight):
        self.__weights[setNum] = weight

    def getWeightsForSet(self, set):
        return self.__weights[set]

    def setReps(self, reps):
        self.__reps = reps

    def getReps(self):
        return self.__reps

    def setRepsForSet(self, setNum, reps):
        self.__reps[setNum] = reps

    def getRepsForSet(self, set):
        return self.__reps[set]

    def getInformationForSet(self, num):
        """
        Returns the information for the parameter set as a Dictionary with:
            - 'set' - the set number
            - 'weight' - the weight
            - 'reps' - the repetitions of the set
        :param num: The set requested
        :raise IndexError: if the requested set is not in range
        :return: Returns a dictionary with 'set', 'weight' and 'reps'
        """
        if num > len(self.__sets):
            raise IndexError

        return {'set': num, 'weight': self.__weights[num], 'reps': self.__reps[num]}

    def getExerciseInformation(self):
        """
        Returns the container object of the exercise
        :return: the container dictionary object of the exercise
        """
        return {"name": self.__name, "sets": self.__sets, "weight": self.__weights, "reps": self.__reps}

    def setHands(self, hands):
        self.__hands = hands

    def getHands(self):
        return self.__hands

    def setWeightMultiplier(self, weightMultiplier):
        self.__weightMultiplier = weightMultiplier

    def getWeightMultiplier(self):
        return self.__weightMultiplier

    def isComplete(self):
        """
        Checks if the Exercise is complete, i.e. if the information for each set is present
        :return: True if the exercise is complete, False otherwise
        """
        return self.__sets == len(self.__weights) \
               and self.__sets == len(self.__reps)

    def isSuperSet(self):
        return self.__superset
