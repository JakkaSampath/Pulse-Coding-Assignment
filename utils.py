from datetime import datetime

def validate_dates(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        if start > end:
            raise ValueError("Start date must be before end date")
    except ValueError as e:
        print("Date Error:", e)
        exit(1)
