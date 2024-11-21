from datetime import datetime, date
import argparse
import uvicorn
import server

class COLORS:
    LIGHT_GREEN: str = "\033[1;32m"
    LIGHT_BLUE: str = "\033[1;34m"
    LIGHT_RED: str = "\033[1;31m"
    END = "\033[0m"


def calculate(date_input: str) -> str:
    date_string = date_input
    past_date: datetime.date = datetime.strptime(date_string, "%Y-%m-%d").date()
    today: datetime.date = date.today()
    days_difference: int = (today - past_date).days
    return str(days_difference)


def get_date():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--date",
        help="date that you would like to calculate time since (Format: YYYY-MM-DD)"
    )
    parser.add_argument(
        "--serve",
        type=int,
        help="port you would like to serve to"
    )

    args = parser.parse_args()
    return args.date, args.serve

def colorify(date_string: str) -> str:
    days_since: str = calculate(date_string)

    if int(days_since) >= 30:
        # Too long
        return f"Days since {date_string}: {COLORS.LIGHT_RED}{days_since}{COLORS.END}"
    else:
        return f"Days since {date_string}: {COLORS.LIGHT_GREEN}{days_since}{COLORS.END}"


if __name__ == "__main__":
    date_input, serve = get_date()
    if serve:
        uvicorn.run(server.app, host="0.0.0.0", port=serve)
    else:
        days_since: str = colorify(date_input)
        print(days_since)