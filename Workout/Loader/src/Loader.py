class Loader(object):
    __filename = ""

    def __init__(self, filename):
        self.__filename = filename

    def changefile(self, newfilename):
        """
        Changes the string filename that the File Reader object holds
        :param newfilename: The string to which the member filename variable will be set
        """
        self.__filename = newfilename

    def read(self):
        """
        Returns the loaded file in a string so that it can be processed,
        this shouldn't be an issue unless the file is extremely long,
        which would be impractical anyways

        :return String containing the whole file contents
        """
        return self.__readfile(self.__filename)

    @staticmethod
    def readfile(self, filename):
        """
        Statically read a file and return it's contents

        :return String containing the whole file contents
        """
        return self.__readfile(filename)

    @staticmethod
    def __readfile(filename):
        """
        Returns the loaded file in a string so that it can be processed,
        this shouldn't be an issue unless the file is extremely long,
        which would be impractical anyways

        :return String containing the whole file contents
        """
        try:
            f = open(filename)
            return f.read()
        except IOError, e:
            print "Failed opening file, error: ", str(e)
