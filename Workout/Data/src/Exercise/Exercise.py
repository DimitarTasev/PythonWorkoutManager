class Exercise(object):
    __container = None

    def __init__(self, name=None, container=None):
        if container is None:
            container = {'name': "", 'sets': 0, 'weight': [], 'reps': []}

        if name is None:
            self.__container['name'] = "Default"

        self.__container = container

    def getName(self):
        """
        :return: String: Returns the exercise name as a string

        """
        return self.__container['name']

    def getSets(self, num):
        """
        Returns the information for the parameter set as a Dictionary with:
            - 'set' - the set number
            - 'weight' - the weight
            - 'reps' - the repetitions of the set
        :param num: The set requested
        :raise IndexError: if the requested set is not in range
        :return: Returns a dictionary with 'set', 'weight' and 'reps'
        """
        if num > len(self.__container['sets']):
            raise IndexError

        return {'set': num, 'weight': self.__container['weight'][num], 'reps': self.__container['reps'][num]}

    def getExerciseInformation(self):
        """
        Returns the container object of the exercise
        :return: the container dictionary object of the exercise
        """
        return self.__container

    def isComplete(self):
        """
        Checks if the Exercise is complete, i.e. if the information for each set is present
        :return: True if the exercise is complete, False otherwise
        """
        return self.__container['sets'] == len(self.__container['weight']) \
               and self.__container['sets'] == len(self.__container['reps'])
