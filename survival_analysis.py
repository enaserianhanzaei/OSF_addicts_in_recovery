import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
import numpy as np
from lifelines import CoxTimeVaryingFitter
import pandas as pd


def KM_estimator(relapsed_data, censored_data):
    durations = relapsed_data + censored_data
    event_observed = list(np.ones(len(relapsed_data))) + list(np.zeros(len(censored_data)))
    ax = plt.subplot(111)
    kmf = KaplanMeierFitter()

    kmf.fit(durations, event_observed, label='kaplan-meier curve')

    axes = plt.gca()
    axes.set_ylim([0, 1])
    axes.set_xlim([0, 86])
    axes.set_position([0.16, 0.175, 0.81, 0.8])

    kmf.plot(show_censors=False, censor_styles={'ms': 3, 'marker': 's'}, ci_show=True, at_risk_counts=False)
    plt.xlabel('Time in Months', labelpad=10, fontsize=20) #, weight='bold'
    plt.ylabel('Survival Probability', labelpad=10, fontsize=20)

    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(15)
        #tick.label1.set_fontweight('bold')
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(15)
        #tick.label1.set_fontweight('bold')

    plt.savefig('km.pdf')
    plt.show()


def unit_timevarying_cox(df, features=[]):
    factors = ['user_id', 'start', 'stop', 'event'] + features
    df_ = df[factors]

    ctv = CoxTimeVaryingFitter()

    ctv.fit(df_, id_col='user_id', event_col='event', start_col='start', stop_col='stop', show_progress=True)
    ctv.print_summary(3)


def cox_hazards_timevarying(df):
    df_subset = df[['user_id', 'start', 'stop', 'richness', 'evenness', 'event']]
    df_nan = df_subset[(df_subset.isnull().any(axis=1)) & (df_subset.event == 1)]

    # dropping rows contain nan
    df_subset = df_subset[~df_subset.user_id.isin(df_nan.user_id.unique())]
    df_subset = df_subset.dropna()

    unit_timevarying_cox(df_subset)
    unit_timevarying_cox(df_subset, ['richness'])
    unit_timevarying_cox(df_subset, ['evenness'])
    unit_timevarying_cox(df_subset, ['evenness', 'richness'])


def main():
    # read the table containing the no of months in recovery for each subject
    time_table = pd.read_csv('data/time_table.csv')
    # identify the number of months of being in recovery for subjects in both cohorts
    relapsed_months, recovered_months = list(time_table.loc[time_table.event == 1].month.values), \
                                        list(time_table.loc[time_table.event == 0].month.values)
    # draw the Kaplan Meier Estimator
    KM_estimator(relapsed_months, recovered_months)

    # reading the file reporting the group activity of users accross Reddit, richness: the number of subreddit a user
    # contributes over the course of recovery, and evenness, how evenly she/he is engaging in those groups.
    multi_group_activity = pd.read_csv('data/activity_during_recovery.csv')
    # applying the extended cox hazard model to identify the effect of factors individually and together on risk of relapse
    cox_hazards_timevarying(multi_group_activity)


if __name__ == '__main__':
    main()
