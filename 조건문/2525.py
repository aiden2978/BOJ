hour, minute = map(int, input().split( ))
duration = int(input())

minuteDone = (minute + duration) % 60
hourDone = hour + int((minute + duration) / 60)

if hourDone >= 24:
    hourDone = hourDone % 24

print(hourDone, minuteDone)