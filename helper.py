import numpy as np
def medal_telly(df):
        medals = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Medal', 'Event'])
        x = medals.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                       ascending=False).reset_index()
        x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
        x['Gold'] = x['Gold'].astype(int)
        x['Silver'] = x['Silver'].astype(int)
        x['Bronze'] = x['Bronze'].astype(int)
        x['total'] = x['total'].astype(int)
        return x

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')
    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')
    return years, country