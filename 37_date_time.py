import datetime

def date_time():

    now = datetime.datetime.now()
    return (str(now.strftime('%Y-%m-%d %H:%M:%S')))

print(f"date_time()\n{date_time()}")