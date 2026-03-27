import pandas as pd

def preprocess(df, region_df):
    # filtering for summer season only
    df = df[df['Season'] == 'Summer']
    # merging with region_df
    df = df.merge(region_df, how='left', on='NOC')
    # dropping the duplicates
    df.drop_duplicates(inplace=True)
    # performing one hot encoding in the medal column
    df = pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)

    return df