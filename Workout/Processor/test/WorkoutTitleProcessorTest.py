import unittest

from Workout.Processor.src.WorkoutTitleProcessor import WorkoutTitleProcessor

class WorkoutTitleProcessorTest(unittest.TestCase):
    dynalistTitle = "!(2016-11-11 11:11 +01:00) @Shoulders 12:22"
    keepTitle = "Shoulders 11/11/2016 11:11 12:22"
    keepShortTitle = "Shoulders 11/11/16 11:11 12:22"

    def test_dynalist(self):
        wtp = WorkoutTitleProcessor(self.dynalistTitle)
        
        # we dont handle date formats in here
        expectedDate = "2016-11-11" 
        expectedTitle = "Shoulders"
        expectedStartTime = "11:11"
        expectedEndTime = "12:22"

        date = wtp.getDate()
        title = wtp.getTitle()
        startTime = wtp.getStartTime()
        endTime = wtp.getEndTime()

        self.assertEqual(expectedDate, date)
        self.assertEqual(expectedTitle, title)
        self.assertEqual(expectedStartTime, startTime)
        self.assertEqual(expectedEndTime, endTime)

    
    def test_keep(self):
        wtp = WorkoutTitleProcessor(self.keepTitle)
        
        # we dont handle date formats in here
        expectedDate = "11/11/2016" 
        expectedTitle = "Shoulders"
        expectedStartTime = "11:11"
        expectedEndTime = "12:22"

        date = wtp.getDate()
        title = wtp.getTitle()
        startTime = wtp.getStartTime()
        endTime = wtp.getEndTime()

        self.assertEqual(expectedDate, date)
        self.assertEqual(expectedTitle, title)
        self.assertEqual(expectedStartTime, startTime)
        self.assertEqual(expectedEndTime, endTime)

    
    def test_keepShort(self):
        wtp = WorkoutTitleProcessor(self.keepShortTitle)
        
        # we dont handle date formats in here
        expectedDate = "11/11/16" 
        expectedTitle = "Shoulders"
        expectedStartTime = "11:11"
        expectedEndTime = "12:22"

        date = wtp.getDate()
        title = wtp.getTitle()
        startTime = wtp.getStartTime()
        endTime = wtp.getEndTime()

        self.assertEqual(expectedDate, date)
        self.assertEqual(expectedTitle, title)
        self.assertEqual(expectedStartTime, startTime)
        self.assertEqual(expectedEndTime, endTime)

    
# Code so that tests can be run as individual files
if __name__ == '__main__':
    unittest.main()