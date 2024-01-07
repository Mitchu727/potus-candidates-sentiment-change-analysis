import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

biden_scores = [52.4, 52.3, 52.4, 52.4, 52.5, 52.2, 52.1, 52.1, 52.0, 52.0, 52.0, 52.3, 51.9, 51.8, 52.0, 52.0, 52.0, 52.0, 51.8, 51.8]
trump_scores = [41.9, 41.8, 41.8, 41.9, 41.7, 41.9, 42.2, 42.2, 42.4, 42.8, 42.9, 42.8, 42.8, 42.9, 43.2, 43.2, 43.4, 43.5, 43.4, 43.4]

start_date = datetime(2020, 10, 15)
end_date = datetime(2020, 11, 3)
dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

plt.figure(figsize=(10, 6))
plt.plot(dates, biden_scores, label='Biden', color='blue')
plt.plot(dates, trump_scores, label='Trump', color='red')

plt.xlabel('Date')
plt.ylabel('Poll Score (%)')
plt.title('Biden vs Trump Poll Scores (Oct 15 - Nov 3, 2020)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.tight_layout()
plt.savefig('poll_scores.png')
plt.show()