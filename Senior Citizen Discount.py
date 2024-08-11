"""
https://www.analystbuilder.com/questions/senior-citizen-discount-fRxVJ?r=UK8yDFMU19J47cYMtTWzLtzkQ

If a customer is 55 or above they qualify for the senior citizen discount. Check which customers qualify.

Assume the current date 1/1/2023.

Return all of the Customer IDs who qualify for the senior citizen discount in ascending order.

customers

customer_id	birth_date
YVD4753692	1989-03-25
XBJ9334631	1964-06-12
CKT7420478	1974-08-26
NRD6336031	1972-07-23
RHY0461182	1951-09-07
UJL8594627	1957-10-10
PLM3202827	1941-06-18
YKL0784996	1984-09-07
WIC7447772	1942-12-14
JWV2386381	1999-05-23
KMA9421058	2013-04-27
GNI7686157	1977-07-12
ZUK8218129	1971-10-11
VNX4490181	1952-02-14
UPB1934369	1968-02-08
MFL8555017	1997-05-22
JYQ0229312	1986-08-25
WCB0774269	1983-06-26
FHX9457768	2012-01-13
QKP2926677	1992-07-24

Field	Data Type
customer_id	text
birth_date	date
"""

import pandas as pd

seniors = customers[(
  (
    (pd.to_datetime('2023-01-01')
     - pd.to_datetime(customers.birth_date))
    .dt.days
  ) // 365.25)
  >= 55
]
seniors[['customer_id']].sort_values('customer_id')
