"""
https://www.analystbuilder.com/questions/bike-price-zKcOR?r=GlQpEkAmHFE0CEkPdIQMdBcM0

Sarah's Bike Shop sells a lot of bikes and wants to know what the average sale price is of her bikes.

She sometimes gives away a bike for free for a charity event and if she does she leaves the price of the bike as blank, but marks it sold.

Write a query to show her the average sale price of bikes for only bikes that were sold, and not donated.

Round answer to 2 decimal places.

inventory
bike_id	bike_price	bike_sold
1001	329.99	Y
1002	99.99	Y
1003	109.99	Y
1004	299.99	Y
1005	NULL	N
1006	329.97	Y
1007	175.99	N
1008	88.99	Y
1009	NULL	Y
1010	125.99	Y
1011	571.99	N
1012	729.99	N
1013	189.99	Y
1014	652.99	N
"""

import pandas as pd

sales_data = inventory[(~inventory.bike_price.isna()) & (inventory.bike_sold=='Y')]

print(round(sales_data.bike_price.mean(), 2))
