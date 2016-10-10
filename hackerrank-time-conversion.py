import sys

def am(t):
    return t[0]+":"+t[1]+":"+t[2] if t[0] != "12" else "00:"+t[1]+":"+t[2]

def pm(t):
    print int(t[0])
    return t[0]+":"+t[1]+":"+t[2] if int(t[0]) >= 12 else str(12+int(t[0]))+":"+t[1]+":"+t[2]

def amANDpm(t, s):
    return (t[0]+":"+t[1]+":"+t[2] if t[0] != "12" else "00:"+t[1]+":"+t[2]) if s == "AM" else (t[0]+":"+t[1]+":"+t[2] if int(t[0]) >= 12 else str(12+int(t[0]))+":"+t[1]+":"+t[2])

time = "07:05:45PM"
# suffix = time[-2:]
# print suffix
# time = time[:-2].split(":")
# suxy = amANDpm(time, suffix) # [2:] to get AM or PM

f = lambda (t, s): t[0]+":"+t[1]+":"+t[2] if t[0] != "12" else "00:"+t[1]+":"+t[2] if s == "AM" else t[0]+":"+t[1]+":"+t[2] if int(t[0]) >= 12 else str(12+int(t[0]))+":"+t[1]+":"+t[2]  
print amANDpm(time[:-2].split(":"), time[-2:])
print f((time[:-2].split(":"), time[-2:]))
