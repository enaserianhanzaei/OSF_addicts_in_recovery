import pandas as pd



def main():
    df = pd.read_csv('./data/table_episodic_modified_conf.csv')
    df['id'] = df.groupby(['user_id']).ngroup()
    df.to_csv('activity_of_addicts_in_recovery.csv', index=False)

    timetable = pd.read_csv('./data/table_episodic_modified_lifetable_conf.csv')
    print(list(df))

    timetable_f = pd.merge(timetable, df[['user_id', 'id']], on='user_id')
    timetable_f.drop_duplicates(inplace=True)

    print(list(timetable_f))
    timetable_f[list(timetable)+['id']].to_csv('time_table.csv', index=False)



if __name__ == '__main__':
    main()
