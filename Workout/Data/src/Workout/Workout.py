# Class containing workout structure
class Workout(object):
    m_name = None
    m_exercises = None
    m_date = None
    m_startTime = None
    m_endTime = None
    m_duration = None

    def __init__(self, name = None):
        if name is not None
            self.m_name = name
        self.m_exercises = []

    def __str__(self):
        string = "Workout name:" + str(self.m_name) + " Date:" + str(self.m_date) + "\nExercises:"

        for exercise in map(str, self.m_exercises):
            string += exercise

        return string

    # Name Functions
    def getName(self):
        """
        :return: The workout name
        """
        return self.m_name

    # Exercise Functions
    def addExercise(self, exercise):
        """
        Appends an exercise to the exercise list
        :param exercise: Exercise to be appended to the list
        """
        self.m_exercises.append(exercise)

    def addAllExercises(self, exercises):
        for exercise in exercises:
            self.addExercise(exercise)

    def getExercise(self, name):
        ex = self.__findExercise(name)

        if ex is None:
            raise "Exercise not found"
        else:
            return self.getExerciseAt(ex)

    def getExerciseAt(self, pos):
        """
        :param pos: The exercise position we're looking for
        :return: Returns the exercise at position pos if pos is in bounds, None otherwise
        """
        return self.m_exercises[pos] if self.__inbounds(pos) else None

    def getAllExercises(self):
        """
        :return: Returns the list containing all of the exercises
        """
        return self.m_exercises

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
            del self.m_exercises[pos]

    def __findExercise(self, name):
        """
        Returns the index of the exercise, or None if not found
        :param name: exercise name to be found
        :return: The index of the exercise in the array,  or None if not found
        """
        for i in range(len(self.m_exercises)):
            e = self.m_exercises[i]
            if name == e.getName():
                return i
        return None

    # Date functions
    def getDate(self):
        return self.m_date

    def setDate(self, date):
        self.m_date = date

    # Duration functions
    def getDuration(self):
        return self.m_duration

    def setDuration(self, date):
        self.m_duration = m_duration
    
    # Start Time functions
    def getStartTime(self):
        return self.m_startTime

    def setStartTime(self, date):
        self.m_startTime = m_startTime
    
    # End Time functions
    def getEndTime(self):
        return self.m_endTime

    def setEndTime(self, date):
        self.m_endTime = m_endTime

    def setTimeData(self, startTime, endTime):
        self.setStartTime(startTime)
        self.setEndTime(endTime)
        # TODO calculate duration

    def count(self):
        return len(self.m_exercises)

    def isEmpty(self):
        return len(self.m_exercises) == 0

    def clear(self):
        self.m_exercises = []

    def __inbounds(self, pos):
        return 0 <= pos < len(self.m_exercises)
