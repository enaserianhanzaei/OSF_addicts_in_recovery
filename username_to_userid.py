import pandas as pd
from params import params


def main():
    df = pd.read_csv('table_episodic_modified_extra.csv')
    df['id'] = df.groupby(['user_id']).ngroup()
    df.to_csv('activity_of_addicts_in_recovery.csv', index=False)

    relap_users_dates = pd.read_csv(params.path_to_data + 'relapsed_users_st_en_dates_nonrestricted.csv')
    recov_users_dates = pd.read_csv(params.path_to_data + 'recovered_users_st_en_dates_nonrestricted.csv')

    relap_users_dates_f = pd.merge(relap_users_dates, df, on='user_id')
    recov_users_dates_f = pd.merge(recov_users_dates, df, on='user_id')

    relap_users_dates_f[list(relap_users_dates)+['id']].to_csv('relapsed_users_st_en_dates.csv', index=False)
    recov_users_dates_f[list(recov_users_dates) + ['id']].to_csv('recovered_users_st_en_dates.csv', index=False)


if __name__ == '__main__':
    main()
