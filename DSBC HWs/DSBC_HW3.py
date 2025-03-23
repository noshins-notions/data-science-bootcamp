import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Problem 1

df['day_name'] = pd.to_datetime(df['hour_beginning']).dt.day_name()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

pedCount = []

for day in weekdays:
    filtered_df = df[df['day_name'].isin([day])]
    day_pedCount = filtered_df.groupby('day_name')['Pedestrians'].sum()
    pedCount.append(day_pedCount)

plt.figure(1)
plt.plot(weekdays, pedCount, color='blue', linewidth=2, marker='o')
plt.title('# OF PEDESTRIANS vs. WEEKDAY')
plt.xlabel('WEEKDAY')
plt.ylabel('# OF PEDESTRIANS')

# Problem 2

nineteen = df[df['hour_beginning'].str.contains('/2019')]

nineteen['weather_summary'] = nineteen['weather_summary'].fillna('unknown')

weathers = nineteen['weather_summary'].unique().tolist()
weather_dict = {weather: index for index, weather in enumerate(weathers)}

nineteen['weather_num'] = nineteen['weather_summary'].map(weather_dict)

pedCount_weather = nineteen.groupby('weather_num')['Pedestrians'].sum()

plt.figure(2)
plt.xticks(range(len(weather_dict)), list(weather_dict.keys()))
plt.plot(range(len(weather_dict)), pedCount_weather, color='blue', linewidth=2, marker='o')
plt.title('Total Pedestrians by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Total Pedestrian Count')
plt.xticks(range(len(weather_dict)), list(weather_dict.keys()), rotation=45)
plt.tight_layout()
plt.show()

# Problem 3

def categorize_time(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

df['time_category'] = pd.to_datetime(df['hour_beginning']).dt.hour.apply(categorize_time)

print(df.time_category)
