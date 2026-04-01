import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Step 1: Create time range from 9 AM to 9 PM at 2-minute intervals
start_time = datetime.strptime("09:00", "%H:%M")
end_time = datetime.strptime("21:00", "%H:%M")
time_slots = [start_time + timedelta(minutes=2*i) for i in range(int((end_time - start_time).seconds / 120))]

np.random.seed(42)
order_counts = np.random.randint(1, 101, size=len(time_slots))

# Step 3: Logic for agents and time
def get_agents_and_time(orders):
    if orders <= 10:
        return 1, "30 sec"
    elif orders <= 50:
        return 2, "1 min"
    else:
        return 3, "2 min"

agents = []
delivery_times = []

for orders in order_counts:
    a, t = get_agents_and_time(orders)
    agents.append(a)
    delivery_times.append(t)

# Step 4: Create DataFrame
df_simulation = pd.DataFrame({
    "Time": [t.strftime("%H:%M") for t in time_slots],
    "Random_Orders": order_counts,
    "Simulated_Agents": agents,
    "Delivery_Time_Est": delivery_times
})

print(df_simulation.head(10))  
