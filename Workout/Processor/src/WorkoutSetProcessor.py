class WorkoutSetProcessor(object):
    def process(self, exerciseSets):
        return self.__processExerciseSetsString(exerciseSets)

    def __processExerciseSetsString(self, exercises):

        """
        Receives the exercise string, at this point would be
        [30*5&15*5] and splits it further sets, so it would
        become [[30*5],[15*5]], signifying 1 set with a superset

        @param exercises::List of string to be processed and split
        @return The weights and reps from the string passed in the parameter
        """

        # split for supersets, does nothing if not superset
        # exercises = [x.split("&") for x in exercises]

        weights = []
        reps = []
        
        for currentSet in exercises:  
            weightsForSet = []
            repsForSet = []

            markedForRepeatWithStarStar = False
            repeatTimes = 0

            # check if set is repeated with **n
            if self.__isRepeatedWithStarStar(currentSet):
                # do what?
                markedForRepeatWithStarStar = True
                repeatTimes = self.__extractRepeatNumber(currentSet)
                currentSet = self.__removeRepeatNumber(currentSet)

            # if repeated, just append last result and that's it
            if self.__isSetRepeatedWithDash(currentSet):
                w, rep = self.__retrieveCache()
                weights.append(w)
                reps.append(rep)
 
            else:  # else process the sets properly
                
                # check and split if a superset
                # otherwise turn into a list anyway for easier processing
                if "&" in currentSet:
                    currentSet = currentSet.split("&")
                else:
                    currentSet = [currentSet]

                # processes a single part of a set, i.e. set1 or set2 if superset
                for setPart in currentSet:  
                    w, rep = self.__processSet(setPart)
                    weightsForSet.append(w)
                    repsForSet.append(rep)

                # fast cache for next set and repeats with **
                self.__cache(weightsForSet, repsForSet)

                if markedForRepeatWithStarStar:
                    # do next thing repeatTimes times
                    w, rep = self.__retrieveCache()
                    for x in range(repeatTimes - 1):
                        weights.append(w)
                        reps.append(rep)

                # append processed weights and set
                weights.append(weightsForSet)
                reps.append(repsForSet)

        return weights, reps

    def __removeRepeatNumber(self, setString):
        s = setString.split(" ")[0]  # splits '25*5 **4' and removes the **4 part
        return s

    def __isRepeatedWithStarStar(self, setString):
        return "**" in setString

    def __extractRepeatNumber(self, setString):
        """
        :return: Number of times the set needs to be added to the weights/reps list, which is number of times repeated - 1
        """
        return int(setString[-1:])

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

            # will return a [[set1], [set2]]
            for drop in dropsets:
                w, rep = self.__processWeightsAndReps(drop)
                weights.append(w)
                reps.append(rep)
        else:
            # handle normal, will return [[set1]]
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
