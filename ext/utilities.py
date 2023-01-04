from datetime import datetime


def parse_float(value: str) -> float:
    try:
        return float(''.join(c for c in value if c.isdigit()))
    except:
        return None


def parse_datetime(value: str) -> datetime:
    try:
        args = value.split()
        day = args[1].replace(",", "")
        month = get_month(args[0])
        year = args[2]
        date_string = f'{day}.{month}.{year}'
        return datetime.strptime(date_string, '%d.%m.%Y')
    except:
        return None


def get_month(m: str) -> int:
    months = ['january', 'february', 'March', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']
    return months.index(m.lower()) + 1
