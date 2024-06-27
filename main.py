from datetime import datetime
from monitor_habits import break_habit
import pandas as pd

habits = [
    break_habit("cigarettes", datetime(2024, 6, 15, 2, 00), cost_per_day = 10, minutes_wasted =  5),
    break_habit("sugar", datetime(2024, 2, 13, 12, 00), cost_per_day = 10, minutes_wasted =  5),
    break_habit("alcohol", datetime(2024, 2, 13, 10, 00), cost_per_day = 10, minutes_wasted =  5),
    break_habit("video games", datetime(2024, 2, 13, 16, 00), cost_per_day = 10, minutes_wasted =  5),
    break_habit("nail biting", datetime(2024, 6, 15, 15, 00), cost_per_day = 10, minutes_wasted =  5),
    break_habit("chocolate", datetime(2024, 6, 12, 19, 00), cost_per_day = 20, minutes_wasted  =10),
]

monitor_habits_df = pd.DataFrame(habits)

monitor_habits_df.to_excel("monitor habits.xlsx", sheet_name="Monitor Habits", index=False)


