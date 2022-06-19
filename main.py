from datetime import datetime, timedelta

users = [

    {
        "name": "Bill", "birthday": "2000-06-21"
    },
    {
        "name": "Katia", "birthday": "2000-06-24"
    },
    {
        "name": "Tamara", "birthday": "2000-06-18"
    },
    {
        "name": "Till", "birthday": "1995-01-10"
    },
    {
        "name": "Jane", "birthday": "2000-06-20"
    },
    {
        "name": "Alex", "birthday": "2000-06-19"
    },
    {
        "name": "Jill", "birthday": "1995-06-23"
    },
    {
        "name": "Yurii", "birthday": "2000-06-22"
    },
    {
        "name": "Nadiia", "birthday": "1995-06-25"
    }
]


def date_range(start, end):
    delta = end - start
    days = [start + timedelta(days=i) for i in range(delta.days)]
    return days


def get_birthdays_per_week(coleegues: list) -> None:
    current_date = datetime.now().date()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    reminder = {}
    start_next_week = current_date - timedelta(days=current_date.weekday()) + timedelta(days=5)
    for col in coleegues:
        this_year_bday = datetime.strptime(col["birthday"], "%Y-%m-%d").replace(year=start_next_week.year).date()
        if this_year_bday in date_range(start_next_week, start_next_week + timedelta(days=7)):
            if this_year_bday.weekday() in [5, 6]:
                if not 0 in reminder.keys():
                    reminder[0] = col['name']
                else:
                    reminder[0] += f", {col['name']}"

            else:
                if not this_year_bday.weekday() in reminder.keys():
                    reminder[this_year_bday.weekday()] = col['name']
                else:
                    reminder[this_year_bday.weekday()] += f", {col['name']}"

    sorted_reminder = {k: v for k, v in sorted(reminder.items())}
    for k, v in sorted_reminder.items():
        print(f"{weekdays[k]}: {v}")


if __name__ == '__main__':
    get_birthdays_per_week(users)
