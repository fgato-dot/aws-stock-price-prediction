import pandas as pd

df = pd.DataFrame({"price": ["10.5", "abc", "30", None]})

df["price"] = pd.to_numeric(df["price"], errors='coerce')

print(df["price"])
# 0    10.5
# 1     NaN   <-- "abc" couldn't convert, became NaN
# 2    30.0
# 3     NaN   <-- None also becomes NaN

import pandas as pd

def transform_data(file):
    df = pd.read_csv(file)
    df = df.dropna()
    df = df[df["amount"] > 0]
    return df.groupby("customer_id")["amount"].sum()