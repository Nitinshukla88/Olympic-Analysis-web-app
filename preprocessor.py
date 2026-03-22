import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

def preprocess():
    global df, region_df
    # filtering for summer season only
    df = df[df['Season'] == 'Summer']
    # merging with region_df
    df = df.merge(region_df, how='left', on='NOC')
    # dropping the duplicates
    df.drop_duplicates(inplace=True)
    # performing one hot encoding in the medal column
    df = pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)

    return df