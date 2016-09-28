# Class containing workout structure
class Workout(object):
    __name = "NotSet"
    __exercises = []
    __date = "NotSet"

    def __init__(self, name):
        self.__name = name
        self.__exercises = []

    def __str__(self):
        string = "Workout name:" + str(self.__name) + " Date:" + str(self.__date) + " Exercises:"

        for exercise in map(str, self.__exercises):
            string += exercise

        return string

    # Name Functions
    def getName(self):
        """
        :return: The workout name
        """
        return self.__name

    # Exercise Functions
    def addExercise(self, exercise):
        """
        Appends an exercise to the exercise list
        :param exercise: Exercise to be appended to the list
        """
        self.__exercises.append(exercise)

    def addAllExercises(self, exercises):
        for exercise in exercises:
            self.addExercise(exercise)

    def getExercise(self, name):
        ex = self.__findExercise(name)

        if ex is None:
            print "Exercise not found"
        else:
            return self.getExerciseAt(ex)

    def getExerciseAt(self, pos):
        """
        :param pos: The exercise position we're looking for
        :return: Returns the exercise at position pos if pos is in bounds, None otherwise
        """
        return self.__exercises[pos] if self.__inbounds(pos) else None

    def getAllExercises(self):
        """
        :return: Returns the list containing all of the exercises
        """
        return self.__exercises

    def removeExercise(self, name):
        """
        Goes through all exercises and finds the one that has the same name, then removes it from the list
        :param name: Exercise to be removed
        """
        ex = self.__findExercise(name)

        # if None then exercise wasn't found
        if ex is None:
            print "Exercise not found"
        else:
            self.removeExerciseAt(ex)

    def removeExerciseAt(self, pos):
        """
        Checks if the input is in bounds and then removes the list at index pos
        :param pos: The index to be removed
        """
        if self.__inbounds(pos):
            del self.__exercises[pos]

    def __findExercise(self, name):
        """
        Returns the index of the exercise, or None if not found
        :param name: exercise name to be found
        :return: The index of the exercise in the array,  or None if not found
        """
        for i in range(len(self.__exercises)):
            e = self.__exercises[i]
            if name == e.getName():
                return i
        return None

    # Date functions
    def getDate(self):
        return self.__date

    def setDate(self, date):
        self.__date = date

    def count(self):
        return len(self.__exercises)

    def isEmpty(self):
        return len(self.__exercises) == 0

    def clear(self):
        self.__exercises = []

    def __inbounds(self, pos):
        return 0 <= pos < len(self.__exercises)
