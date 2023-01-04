from enum import Enum


class Rating(Enum):
    EXCELLENT = 'excellent'  # sum of points => 80%
    GOOD = 'good'  # 60% <= sum of points < 80%
    SATISFACTORY = 'satisfactory'  # 40% <= sum of points < 60%
    UNSATISFACTORY = 'unsatisfactory'  # sum of points < 40%
    NULL = 'null'


def get_rating(value: float) -> Rating:
    try:
        percent = float(value) / 20
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
