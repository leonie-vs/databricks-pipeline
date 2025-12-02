import pandas as pd

# read in parquet data
raw_yellow = pd.read_parquet('data/yellow_tripdata_2025-09.parquet')
print(raw_yellow.head(5))

# create vendors dataframe that maps vendor_name to vendor_id
vendors = {"vendor_id": [1, 2, 6, 7], "vendor_name": ["Creative Mobile Technologies, LLC", "Curb Mobility, LLC", "Myle Technologies Inc", "Helix"]}
vendor = pd.DataFrame(data=vendors)
vendor = vendor.set_index('vendor_id')
print(vendor.head(5))

vendor.to_csv('data/vendors.csv')

# create rate_code dataframe that maps rate_code_id to the final rate code in effect at the end of the trip
rate_code = {"rate_code_id": [1, 2, 3, 4, 5, 6, 99], "final_rate": ["Standard rate", "JFK", "Newark", "Nassau or Westchester", "Negotiated fare", "Group ride", "Null/unknown"]}
rate_codes = pd.DataFrame(data=rate_code)
rate_codes = rate_codes.set_index('rate_code_id')
print(rate_codes.head(5))

rate_codes.to_csv('data/rate_codes.csv')

# create payment dataframe that maps payment_id to payment_type
payment_types = {"payment_id": [0, 1, 2, 3, 4, 5, 6], "payment_type": ["Flex Fare trip", "Credit card", "Cash", "No charge", "Dispute", "Unknown", "Voided trip"]}
payment = pd.DataFrame(data=payment_types)
payment = payment.set_index('payment_id')
print(payment.head(5))

payment.to_csv('data/payment.csv')

