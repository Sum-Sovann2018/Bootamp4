import datetime

def currect_date():

    now = datetime.datetime.now()
    return (str(now.strftime('%Y-%m-%d')))

print(f"current_date()\n{currect_date()}")