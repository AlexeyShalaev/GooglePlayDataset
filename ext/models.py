from enum import Enum
from datetime import datetime


class Rating(Enum):
    EXCELLENT = 5  # sum of points => 80%
    GOOD = 4  # 60% <= sum of points < 80%
    SATISFACTORY = 3  # 40% <= sum of points < 60%
    UNSATISFACTORY = 2  # sum of points < 40%
    NULL = 0


def get_rating(value: float) -> Rating:
    try:
        percent = float(value) / 5
        if percent < 0.4:
            return Rating.UNSATISFACTORY
        elif percent < 0.6:
            return Rating.SATISFACTORY
        elif percent < 0.8:
            return Rating.GOOD
        else:
            return Rating.EXCELLENT
    except:
        return Rating.NULL


class Season(Enum):
    WINTER = 'winter'  # Зима
    SPRING = 'spring'  # Весна
    SUMMER = 'summer'  # Лето
    AUTUMN = 'autumn'  # Осень
    NULL = 'null'


def get_season(date: datetime) -> Season:
    month = date.month
    if month == 12 or month <= 2:
        return Season.WINTER
    elif month <= 5:
        return Season.SPRING
    elif month <= 8:
        return Season.SUMMER
    elif month <= 11:
        return Season.AUTUMN
    else:
        return Season.NULL
