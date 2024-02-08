import pytz
from datetime import datetime

mexico_city_timezone = pytz.timezone("America/Mexico_City")


def now() -> datetime:
    return datetime.now()


def local_datetime() -> datetime:
    return datetime
