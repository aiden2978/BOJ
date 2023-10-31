hour, minute = map(int, input().split( ))
hourEarly = 0
minuteEarly = 0

if minute >= 45:
    hourEarly = hour
    minuteEarly = minute - 45
else:
    if hour >= 1:
        hourEarly = hour - 1
        minuteEarly = minute + 15
    else:
        hourEarly = 23
        minuteEarly = minute + 15

print(hourEarly, minuteEarly)