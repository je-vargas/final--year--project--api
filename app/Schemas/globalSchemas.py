from enum import Enum

class WorkHoursSchema(str, Enum):
    sixMore = '6+',
    fourMore = '4-6',
    twoMore = '2-4',
    zeroMore = '0-2',