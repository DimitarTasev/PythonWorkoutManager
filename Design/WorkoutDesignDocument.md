Design Document
<> required, () optional, ... can handle multiple

Workout format:
    Name:
    Style 1: (dynalist style)
        TODO -> <!(dynalist<->style<->date (start time<:>dynalist style)>;<@Workout name>;(end time or duration)
        TODO -> <!(2016-09-21 18:00 +01:00)>;@Legs;1:32 -> 1h 32min duration, if end time < start time, then user input is pure duration
        TODO -> <!(2016-09-21 18:00 +01:00)>;@Legs;18:32 -> 32min duration, if end time > start time, then user input is end time, so we must calculate duration (end time - start time) IF ONLY HOURS HAD 100 MINUTES THO (only works in 24h style, but no one likes 12h format anyway, if we need to support just convert to 24h for ease)
    
    #Style2: (easier for phones and keep)
        TODO -> <@Workout name><; or whitespace><day-month-year></ or whitespace><start time></ or whitespace><end time or duration>
        TODO -> @Legs 03-10-2016 18:30 19:30
        TODO -> @Legs 03-10-2016 18:30 1:30
        TODO -> @Legs/03-10-2016/18:30/19:30
        TODO -> @Legs/03-10-2016/18:30/1:30


    Exercise format:

    <set name>(& <super set name>...)(<; or whitespace><set count>/(hands)/(<*>weight multiplier)) -> Overhead Press;5/2/*1
        DONE -> Overhead Press;5/2/*1
        DONE -> Overhead Press;5/2
        DONE -> Overhead Press;5
        DONE -> Overhead Press -> can now calculate the amount of sets
        DONE -> Exercise & Super set
        TODO -> Overhead Press 5/2/*1 -> support whitespace for ease

    <_ or kgs><* or x><reps>(, <kgs <* or x><reps>...)(& <kgs><* or x><reps>...)(**# of sets it was repeated)
        DONE -> _*10 -> 10 reps with body weight
        DONE -> _*10&_*10
        DONE -> 30*5 -> normal set
        DONE -> 30*5,15*5 -> dropset
        DONE -> 30*5&15*5 -> superset
        DONE -> 30*5,15*5&15*5,7.5*5 -> super drop set
        TODO -> 30*5&15*5 **4 -> same repeated for a total of 4 sets (or for the next n-1 sets)
    or 

        DONE <-> to copy same kgs/reps as above -> -
        TODO_low_priority -> 30*- -> format for same reps
        TODO_low_priority -> -*30 -> format for same kgs