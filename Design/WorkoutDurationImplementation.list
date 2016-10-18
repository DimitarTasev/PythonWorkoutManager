Need to figure out which style we're using
    if dynalist
    or keep

Done: processing dynalist
    crop out the data from between !(...) 
        can check if it has time start or not depending on length
            maybe we should enforce start time and duration
        
    after it's been cropped, we can split by whitespace and we should get array of len 3
        first is the date, a constant of 10 characters
        second is the start time, a constant of 5 characters3 hh:mm
        third one we dont care about(for now), because it's the time zone
    
    the rest of the string (without the !(...)) can again be split by whitespace and we get array if len 2 with
        1:the workout name, with the @symbol that dynalist uses for tags
        2:the duration or end time, has to be processed depending on whether duration > (means end time given) or < (means duration given) than start time
            can foresee problems with midnight workouts
                if u started at midnight then, we can assume it's end time (doesnt always work)
                    st: 00:25 et: 01:24
                        problem we meant 59 minute workout or 1h 49m woorkout, it's ambiguous
            can maybe solve it my using h:mm for duration and hh:mm for end times
                could work but might need to be changed in the future
            could add symbol d for duration in front d1:34 -> duration was 1h 34mins
                and e for end time e1:34 -> ended at 1:34 (24h clock)

    dynalist can be used to enforce a 24h clock, but we have the conversion algorithm too

Done: processing keep
    more straightforward as it's supposed to be easily writable with a phone
    split the string by whitespace 
        we should have 3 array members 
            workout name
            start time
            end time/duration   
                same problems with endtime/duration as with dynalist

#duration in workout
            calculate duration from end time - start time (not as easy as it sounds)
            if end time < start time:
              - duration is provided and we can use it
            else:
              - duration is not provided and we must calculate it using end time - start time
            12h format? for the future, but if we encounter 12h format just convert to 24h