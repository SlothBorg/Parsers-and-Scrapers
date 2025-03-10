from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

FIRST_DATE = '2023-11-11 00:00:00'
SECOND_DATE = '2024-09-21 00:00:00'
DATES = [
    FIRST_DATE,
    SECOND_DATE
]


def get_year_dats_offset(date_1, date_2):
    years_to_add = date_2.year - date_1.year
    start_date_plus_year = date_1 + relativedelta(years=years_to_add)
    year_days_delta = start_date_plus_year - date_1

    return year_days_delta.days


def get_days_offset(date_1, date_2):
    day_delta = date_2 - date_1

    return day_delta.days


def add_time(start_date, time_to_subtract):
    # kwargs = {time_unit: time_to_subtract}
    # return start_date + timedelta(**kwargs)
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")

    return start_date + timedelta(days=time_to_subtract)


if __name__ == "__main__":
    counter = 0

    start_datetime = datetime.strptime(FIRST_DATE, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(SECOND_DATE, "%Y-%m-%d %H:%M:%S")

    # 366
    year_day_count = get_year_dats_offset(start_datetime, end_datetime)
    # 315
    starting_day_delta = get_days_offset(start_datetime, end_datetime)
    # 51
    days_to_subtract = year_day_count - starting_day_delta

    # for the next iteration
    time_to_add = starting_day_delta - days_to_subtract

    # loop this:
    while True:
        if time_to_add > 0:
            next_date = add_time(DATES[-1], time_to_add)
            time_to_add = time_to_add - days_to_subtract
        else:
            break

        DATES.append(next_date)

    for date in DATES:
        print(date)
