from datetime import datetime, date
import argparse

class Colors:
    light_green = "\033[1;32m"
    light_blue = "\033[1;34m"
    light_red = "\033[1;31m"
    end = "\033[0m"


def calculate(date_input: str) -> str:
    date_string = date_input
    past_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    today = date.today()
    days_difference = (today - past_date).days
    # print(f"Days since {date_string}: {days_difference}")
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

def colorify():
    date_string = get_date()
    days_since = calculate(date_string)

    if int(days_since) >= 30:
        # Too long
        return f"Days since {date_string}: {Colors.light_red}{days_since}{Colors.end}"
    else:
        return f"Days since {date_string}: {Colors.light_green}{days_since}{Colors.end}"

if __name__ == "__main__":
    days_since = colorify()
    print(days_since)
