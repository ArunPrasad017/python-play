def angleClock(hour,min):
    hour_angle = (hour%12+min/60) *30
    min_angle = min*6
    val = int(abs(hour_angle-min_angle))
    if val>180:
        return 360-val
    return val

print(angleClock(12,30))