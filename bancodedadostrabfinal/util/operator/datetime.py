import datetime
from typing import Union

import pytz
from dateutil.parser import parse


class Datetime:
    """docstring for Datetime."""

    datetime = datetime

    @staticmethod
    def timezone():
        return pytz.timezone("America/Sao_Paulo")

    @staticmethod
    def now():
        return Datetime.timezone().localize(datetime.datetime.now())

    @staticmethod
    def timeShift(**kwargs):
        if "year" not in kwargs:
            year = datetime.datetime.now().year
            kwargs.update({"year": year})

        if "month" not in kwargs:
            month = datetime.datetime.now().month
            kwargs.update({"month": month})
        return Datetime.timezone().localize(datetime.datetime(**kwargs))

    @staticmethod
    def parseDate(timestr: Union[datetime.datetime, datetime.date, str]) -> datetime.date:

        if isinstance(timestr, datetime.datetime):
            return timestr.date()
        elif isinstance(timestr, datetime.date):
            return timestr
        return parse(timestr).date()

    @staticmethod
    def parseDatetime(timestr: Union[datetime.datetime, datetime.date, str]) -> datetime.datetime:

        if isinstance(timestr, datetime.datetime):
            return timestr
        elif isinstance(timestr, datetime.date):
            return datetime.datetime(timestr.year, timestr.month, timestr.day)
        return parse(timestr)

    @staticmethod
    def humanizeTime(amount: float, units: str) -> str:
        """Divide `amount` in time periods.
            Useful for making time intervals more human readable.

        Args:
            amount (float): value time
            units (str): value unit

        Returns:
            str: time human readable
        """

        intervals = [
            1,
            1000,
            1000000,
            60000000,
            3600000000,
            86400000000,
            604800000000,
            2419200000000,
            29030400000000,
        ]
        names = [
            ("us", "us"),
            ("ms", "ms"),
            ("s", "s"),
            ("min", "min"),
            ("h", "h"),
            ("day", "days"),
            ("week", "weeks"),
            ("month", "months"),
            ("year", "years"),
        ]
        result = []

        unit = list(map(lambda a: a[1], names)).index(units)
        # Convert to seconds
        amount = amount * intervals[unit]

        for i in range(len(names) - 1, -1, -1):
            a = amount / intervals[i]
            if int(a) > 0:
                result.append((a, names[i][1 % int(a)]))
                amount -= a * intervals[i]

        return f"{result[0][0]:.2f} {result[0][1]}" if len(result) > 0 else ""
