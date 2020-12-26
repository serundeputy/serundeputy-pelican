import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cdc.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cdc.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# https://data.cdc.gov/resource/9mfq-cb36.json?submission_date=2020-07-09T00:00:00.000
results = client.get("9mfq-cb36", submission_date='2020-07-09T00:00:00.000')

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

#print(results_df.head())
#print(results_df.describe())

print(results_df['new_case'].sum())
