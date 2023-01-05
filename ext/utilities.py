from datetime import datetime


def parse_float(value: str) -> float:
    try:
        return float(''.join(c for c in value.replace(',', '.') if c.isdigit() or c == '.'))
    except:
        return None


def parse_integer(value: str) -> int:
    try:
        return int(''.join(c for c in value if c.isdigit()))
    except:
        return None


def parse_literal(value: str) -> float:
    try:
        literal = value[-1]
        if literal == 'M':
            return parse_float(value) * 10 ** 6
        elif literal == 'k':
            return parse_float(value) * 10 ** 3
        elif value == 'Varies with device':
            return 0
        else:
            return parse_float(value)
    except:
        return 0


def erase_extra(value: str) -> str:
    try:
        return ''.join(c for c in value.replace(',', '.') if c.isdigit() or c == '.')
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


def get_installs_grade(installs: int) -> float:
    try:
        arr = [1000, 5000, 10000, 50000, 100000, 500000, 10 ** 6, 10 ** 7, 10 ** 8, 10 ** 9]
        for i in range(len(arr)):
            if installs <= arr[i]:
                return min(((i + 1) / 5) * (installs / arr[i]) * 10, 10)
    except:
        return 0
    return min(10 * installs / 10 ** 9, 10)
