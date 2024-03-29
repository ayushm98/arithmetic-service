import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Re-analyzing the observation notes with the correct durations and mapping them to the enclosure map

# Observations for Orangutan A (each '.' is 1 minute, '-' indicates behavior change)
obs_A = '.....-.....-.....-.....-.....-.....-.....-.....-.....'  # Represents 45 minutes of behavior
# Translating behavior observation to the enclosure map (heights are arbitrary for this example)
map_A = {
    '.': 0,  # Unspecified behavior (could be ground level)
    'R_in': 2,  # Right side, inside (perhaps a platform or enclosure feature)
    'R_out': 1,  # Right side, outside (ground level but different zone)
    # Add other behaviors as necessary
}
heights_A = [map_A.get(b, 0) for b in obs_A if b in map_A]  # Get heights for each minute observed

# Observations for Orangutan K
obs_K = '.....-.....-.....-.....-.....-.....-.....-.....-.....'  # Represents 45 minutes of behavior
# Map for Orangutan K
map_K = {
    '.': 0,  # Unspecified behavior
    'LIR_in': 3,  # Left Interior Region, inside
    'LIR_out': 1.5,  # Left Interior Region, outside
    # Add other behaviors as necessary
}
heights_K = [map_K.get(b, 0) for b in obs_K if b in map_K]  # Get heights for each minute observed

# Create a list of datetime objects for each minute
start_time = datetime.strptime('11:45', '%H:%M')
time_list = [start_time + timedelta(minutes=i) for i in range(45)]

# Plotting the behaviors over time
fig, ax = plt.subplots(figsize=(15, 6))

ax.plot(time_list, heights_A, color='blue', marker='o', linestyle='-', label='Orangutan A')
ax.plot(time_list, heights_K, color='green', marker='o', linestyle='-', label='Orangutan K')

# Formatting the plot
ax.set_title('Activity Over Time for Orangutans A and K')
ax.set_xlabel('Time')
ax.set_ylabel('Height/Activity Level')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
fig.autofmt_xdate()
ax.legend()
ax.grid(True)

plt.show()
