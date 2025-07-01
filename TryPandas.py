import pandas as pd
URL = 'https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm'
tables = pd.read_html(URL)
df = tables[0]
print(df)