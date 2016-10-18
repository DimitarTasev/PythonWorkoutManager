 Goal:
The goal of the Workout Analyzer is to provide the means to track progress over time
Can check versus last workout
Can check versus statistics over time for a workout group
    workout groups:
        legs
        arms
        shoulders
        chest
        core
Progress over time definition:
    Weight/rep increase over time
        calculate the % increase since last workout for the workout group
        calculate the % increase since first entry for the workout group

Duration tracking
    duration related to number of exercises in the workouts 
        same duration, less exercises*reps is worse
        sets/exercise ratio of over 0.8 is good
        we want a similar ratio or higher ratio for similar durations
    how do shorter and longer workouts affect any consecutive workouts
        does a longer workouts (>1h30min) affect the rest consecutive workouts (until rest day)
    
Weights/Reps 
    start time  
        group workouts by start time range
        compare workouts of same type vs a different start time range 
            i.e. shoulders at 10am-11am vs shoudlers at 3pm-4pm
                show % difference between them
    Order of workouts
        track how progress is compared to the last workout of the same type by taking the order into account 
            note where a lower performance is available compared to the previous and note what the previous workout sequence is on this occurence and on the previous
                look for any significant changes (>5%?)

Workout Difficulty Adjustment/Calculation
    variables:
        exercises count
        sets per exercise
        duration
        weights related to PR
        reps related to PR

The progress includes:
    Information tracked/computed:
        - weight
        - reps
        - weight increase over time
        - repetition increase over time
        - rest change between exercises over time (need to support rest tracking)
        - weight/reps as related to:
            - workout order (e.g. chest > legs > shoulders, in theory shoulders should be stronger than in chest > shoudlers)
            - workout start time (need to add time support, can add in title)
                - morning workouts in theory should be lower weights/more reps (or plain cardio)
                - afternoon/evening workouts in theory should be higher weights
            - workout duration (need to support duration, can add in title)
                - how does longer duration affect the workout
                - how does shorter duration affect the workout
            - how does the workout duration affect consecutive workouts 
                - longer workouts could tire you more, leading to lower performance in consecutive workouts

Means to export to:
    - CSV
    - excel spreadsheet
Means to graph data:
    - using matlab
    - some other plotting library
