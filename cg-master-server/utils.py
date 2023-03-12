from datetime import datetime

def timeNow():

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return date

