from datetime import datetime


async def current_date_time():
    current_date_time = datetime.now()

    current_date = current_date_time.date()
    current_time = current_date_time.time().strftime("%H:%M:%S")

    return {"current_date": str(current_date), "current_time": current_time}
