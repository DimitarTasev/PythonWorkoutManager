TODO check if ; messes up dynalist

TODO features:
    - new repeated workouts format
    - rest tracking
        - need to add in WorkoutDesignDocument
            - if only 1 number (i.e. 30, 60, 90, 120) assume seconds
            - if format m:sec (i.e. 1:20, 2:00) process minutes:seconds
        - need to support 
            - rest after set

    - duration for workout
        - outlined format in WorkoutDesignDocument:
        - #start_time in workout name #Style2
        - #duration in workout
            - calculate duration from end time - start time (not as easy as it sounds)
            - if end time < start time:
                - duration is provided and we can use it
            - else:
                - duration is not provided and we must calculate it using end time - start time
            - 12h format? for the future, but if we encounter 12h format just convert to 24h 

TODO_low_priority:
    - support whitespace to separate workout and workout information (line 18 in WorkoutDesignDocument)
    - support '-' as re-use from cache for ONLY weights or reps