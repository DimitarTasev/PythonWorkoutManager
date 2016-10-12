TODO refactoring:
    split processor into #9
        workout exercise processor
        done: workout title procesor
    
TODO data handling:
    add date class #10
        write implementation document
        will handle all date and time stuff for workout
    
    add duration class
        

TODO features:
    new repeated workouts format #11

    duration for workout #7
        outlined format in WorkoutDesignDocument
        outlined implementation in WorkoutDurationImplementation 

TODO_low_priority:
    support whitespace to separate workout and workout information (line 18 in WorkoutDesignDocument)
    support '-' as re-use from cache for ONLY weights or reps

Cancelled:
    rest tracking
    need to add in WorkoutDesignDocument
        if only 1 number (i.e. 30, 60, 90, 120) assume seconds
        if format m:sec (i.e. 1:20, 2:00) process minutes:seconds
    need to support 
        rest after set
