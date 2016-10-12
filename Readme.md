TODO check if ; messes up dynalist

TODO features:
    - new repeated workouts format

    - duration for workout
        - outlined format in WorkoutDesignDocument
        - outlined implementation in WorkoutDurationImplementation 

TODO_low_priority:
    - support whitespace to separate workout and workout information (line 18 in WorkoutDesignDocument)
    - support '-' as re-use from cache for ONLY weights or reps

Cancelled:
    - rest tracking
    - need to add in WorkoutDesignDocument
        - if only 1 number (i.e. 30, 60, 90, 120) assume seconds
        - if format m:sec (i.e. 1:20, 2:00) process minutes:seconds
    - need to support 
        - rest after set
