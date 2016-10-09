TODO check if ; messes up dynalist
        
TODO add support in workout definition in file:
    - rest tracking
    - start time in workout
        - use dynalist style
            - need to change current format handling
            - change title style 
                - separate everything with ; <- really annoying to do on keep, and using whitespace is better
                - OR just look for !( and ) and cut it off, then process separately
                    - python split on ')'?
                - how do we separate workout title and time?
                    - workout is always @Name_here
                        - we can separate on whitespace?
                            - split(' ')
                - OR we could just split the whole thing on whitespace and pray for 3 members [date + start time, workout name, end time]
                    - if len > 3 then process end time
                        - handle using #duration

    - #duration in workout
        - calculate duration from end time - start time (not as easy as it sounds)
        - if end time < start time:
            - duration is provided and we can use it
        - else:
            - duration is not provided and we must calculate it using end time - start time
        - 12h format? for the future, but if we encounter 12h format just convert to 24h 
