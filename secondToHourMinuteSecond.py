def getHourMinuteSecond(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return (f"{hours}:{minutes}:{seconds}")