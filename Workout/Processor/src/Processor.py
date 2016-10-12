from Workout.Loader.src.Loader import Loader
from Workout.Data.src.Workout.Workout import Workout
from Workout.Data.src.Exercise.Exercise import Exercise
from Workout.Processor.src.WorkoutExerciseProcessor import WorkoutExerciseProcessor
from Workout.Processor.src.WorkoutTitleProcessor import WorkoutTitleProcessor


class Processor(object):
    """
    Process the loaded file string into a Workout
    """
    m_fileContents = None
    m_lastWorkout = None

    def __init__(self, filecontents=None):
        if filecontents is not None:
            self.m_fileContents = filecontents

    def setWorkoutFileContents(self, workoutFileContents):
        self.m_fileContents = workoutFileContents

    def clearMemory(self):
        """
        Removes the information from the contents string
        """
        self.m_fileContents = ""

    def process(self):
        """
        :return: A list of Workout objects containing all of the workouts in the file
        """
        print "Starting processing"

        if len(self.m_fileContents) < 1:
            raise Exception("No workout provided in file. Please set one in constructor or using \
            setWorkoutText()")

        self.m_fileContents = self.m_fileContents.splitlines()

        self.m_lastWorkout = self.__createWorkout(self.m_fileContents)

        return self.m_lastWorkout

    def __createWorkout(self, fileContents):
        titleAndDate = fileContents[0]

        titleProcessor = WorkoutTitleProcessor(titleAndDate)
        exerciseProcessor = WorkoutExerciseProcessor(fileContents[1:])

        workout = Workout(titleProcessor.getTitle())
        workout.setDate(titleProcessor.getDate())

        # todo will need to separate workouts at some point #4
        workout.addAllExercises(exerciseProcessor.getAllExercises())

        return workout

