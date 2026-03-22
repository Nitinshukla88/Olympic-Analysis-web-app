def medal_telly(df):
        medals = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Medal', 'Event'])
        x = medals.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                       ascending=False).reset_index()
        x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
        return x