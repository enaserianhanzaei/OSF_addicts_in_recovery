Here, we explain each data file and the included features in them.

(1) recovered_users_st_en_dates.csv
This data file containe the information, recovery start date and last recovery announcmenet, of addicts who reported their recovery progress and haven't mentioned their relapse.


(2) relapsed_users_st_en_dates.csv
This data file containe the information, recovery start date and relapse date, of addicts who reported their recovery progress and have mentioned their relapse.


(3) activity_during_recovery.csv
This file contains the activity of the addicts in Reddit in terms of group membership. We created the file in a copatible format for the lifeline survival analysis. lifelines requires that the dataset be in what is called the long format. This looks like one row per state change, including an ID, the left (exclusive) time point, and right (inclusive) time point. 

In the above dataset, start and stop denote the boundaries, user_id is the unique identifier per individual, and event denotes if the subject relapsed at the end of that period. 
Richness is the number of subreddit a user is a part of, and evenness in how evenly she/he is engaging in them.







