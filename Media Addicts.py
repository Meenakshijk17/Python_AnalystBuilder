"""
https://www.analystbuilder.com/questions/media-addicts-deISZ?r=Ji7KH4dU3mCPYxJMKz0DKVF0h

Social Media Addiction can be a crippling disease affecting millions every year.

We need to identify people who may fall into that category.

Write a query to find the people who spent a higher than average amount of time on social media.

Provide just their first names alphabetically so we can reach out to them individually.

user_time
Field	Data Type
user_id	int
media_time_minutes	int

users
Field	Data Type
user_id	int
first_name	text
"""

import pandas as pd

avg_media_time_minutes = user_time.media_time_minutes.mean()
user_time = user_time[user_time.media_time_minutes > avg_media_time_minutes]
full_df = user_time.merge(users, on='user_id', how='left')
full_df = full_df.sort_values(['first_name'])
full_df[['first_name']]
