# TODO this class will have the exercise processing bits from the processor

class WorkoutTitleProcessor(object):
    m_titleAndDate = None
    m_title = None
    m_date = None
    m_startTime = None
    m_endTime = None

    def __init__(self, titleAndDate = None):
        if titleAndDate is not None:
            self.m_titleAndDate = titleAndDate

        self.__process(self.m_titleAndDate)

    def __process(self, titleAndDate):
        # determine dynalist or keep format
        # both require a split on whitespace

        if self.__isDynalistDate(titleAndDate):
            self.__processDynalist(titleAndDate)
        else:
            self.__processKeep(titleAndDate)
            

        # titleAndDate = title.split("@")
        # date = titleAndDate[0]
        # title = titleAndDate[1]

    def __splitDate(self, titleAndDate, separator = " "):
        return titleAndDate.split(separator)

    def __isDynalistDate(self, titleAndDate):
        """
        Simple check to see if the name has an @ in it

        :return: True if name has @, False otherwise
        """
        return ("@" in titleAndDate)

    def __processDynalist(self, titleAndDate):
        """
        Handle dynalist format: !(YYYY-MM-DD HH:MM +HH:MM) @Title HH:MM
        """
        # strip excess !( and )
        titleAndDate = titleAndDate.translate(None, "!()")
        # split on whitespace, get 3 members, year, start time, end time/duration  
        titleAndDate = self.__splitDate(titleAndDate)

        self.m_title = titleAndDate[3][1:]  # this removes the @ sign
        self.m_date = titleAndDate[0]
        self.m_startTime = titleAndDate[1]
        self.m_endTime = titleAndDate[4]
        # timeZone = titleAndDate[2] # we dont care about that right now 
    
    def __processKeep(self, titleAndDate):
        """
        Handle keep format: Title DD/MM/YYY HH:MM HH:MM
        """
        titleAndDate = self.__splitDate(titleAndDate)

        self.m_title = titleAndDate[0] # this removes the @ sign
        self.m_date = titleAndDate[1]
        self.m_startTime = titleAndDate[2]
        self.m_endTime = titleAndDate[3]


    def getTitle(self):
        return self.m_title

    def getDate(self):
        return self.m_date
    
    def getStartTime(self):
        return self.m_startTime

    def getEndTime(self):
        return self.m_endTime
    