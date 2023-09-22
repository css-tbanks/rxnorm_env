import re
import pandas as pd

def df_clean(df):
    df.fillna(0, inplace=True)  # fill missing values with 0
    df.drop_duplicates(inplace=True)

    # removing non-ascii, spaces, carriage returns from columns
    df.columns = [col.encode('ascii', 'ignore').decode('utf-8').replace('\r', '').replace(' ', '_') for col in df.columns] # headers
    df = df.map(lambda x: re.sub(r'[^\x00-\x7F]+', '', str(x))) # body
    
    # data type conversion
    # df['numeric_column'] = df['numeric_column'].astype(float)
    # df['date_column'] = pd.to_datetime(df['date_column'])

    return df
