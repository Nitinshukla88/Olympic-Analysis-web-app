def medal_telly(df):
        medal_telly = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Medal', 'Event'])
        x = medal_telly.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                       ascending=False).reset_index()
        x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
        return x