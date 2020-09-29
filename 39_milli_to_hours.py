
import datetime
def milli_to_hours(millis):

    millis = int(millis)

    seconds=(millis/1000)%60
    seconds = int(seconds)

    minutes=(millis/(1000*60))%60
    minutes = int(minutes)

    hours=(millis/(1000*60*60))%24

    return f"milli_to_hours({millis})\n{int(hours)}"

print(milli_to_hours(10800000))