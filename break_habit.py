from datetime import datetime

goal = 60       #number of days it takes roughly to make or break a habit

def break_habit(habit_name, start_date, cost_per_day, minutes_wasted):

    date = start_date.strftime("%d %B %Y")

    # Total time elapsed in seconds
    time_elapsed = (datetime.now() - start_date).total_seconds()
    # .total_seconds() converts the duration into seconds

    # Convert the time in seconds into hours / days.
    hours = round(time_elapsed / 60 / 60, 2)
    days = round(hours / 24, 2)

    # calculating day streak
    streak = int(days)

    # calculating money and time saved
    money_saved = int(cost_per_day * days)
    time_saved = int(minutes_wasted * days)

    # calculating days remaining to break that habit
    days_remaining = int(goal - days)

    # after the goal of 60 days is completed
    if days_remaining <= 0:
        days_remaining = 0

    return {
        "Habit To Break": habit_name.title(),
        "Date Started" : date,
        "Streak(days)" : streak,
        "Time Saved(minutes)" : time_saved,
        "Money Saved" : money_saved,
        "Days Remaining / 60" : days_remaining
    }

