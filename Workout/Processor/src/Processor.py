from Workout.Loader.src.Loader import Loader


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

    def readFile(self):
        try:
            self.__contents = self.__fr.read()
        except IOError, e:
            raise IOError(e)

    def process(self):
        """
        :return: A list of Workouts containing all of the workouts in the file
        """
        print "Starting processing"
        if self.__contents is None:  # load the file if it hasnt been loaded yet
            try:
                self.readFile()
            except IOError, e:
                print "Failed opening file" + str(e)
                return
                # raise IOError("Failed opening file" + str(e))

        if len(self.__contents) < 1:
            raise Exception("File is empty")
        self.__contents = self.__contents.splitlines()
        return self.__contents

    def __processString(self, string):
        # easy to process string array, first is title, and so on

r = Processor("../../TestData/ShoulderWorkout.txt")
print r.process()