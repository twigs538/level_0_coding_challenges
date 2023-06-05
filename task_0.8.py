def hours_and_minutes(num):
    hours = num // 60
    minutes = num % 60
    hours_string = "hour"
    minutes_string = "minute"

    if hours != 1:
        hours_string = "hours"
    if minutes != 1:
        minutes_string = "minutes"
    result = f"{hours} {hours_string}, {minutes} {minutes_string}"
    return result

print(hours_and_minutes(71))
print(hours_and_minutes(133))