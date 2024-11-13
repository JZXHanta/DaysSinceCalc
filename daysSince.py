from datetime import datetime, date
import argparse


def calculate(date_input: str) -> str:
    date_string = date_input
    past_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    today = date.today()
    days_difference = (today - past_date).days
    print(f"Days since {date_string}: {days_difference}")
    return str(days_difference)


def get_date() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "date",
        help="date that you would like to calculate time since (Format: YYYY-MM-DD)"
    )

    args = parser.parse_args()
    date = args.date
    return date


if __name__ == "__main__":
    date_string = get_date()
    days_since = calculate(date_string)
