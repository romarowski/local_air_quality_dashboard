from data import convert_limits
from datetime import datetime
import pdb
def values(poll_df, station='Privet Aviation', regulator='SA'):
    maxi = max(poll_df['To Date'])
    obj = datetime.strptime(maxi, '%Y-%m-%d %H:%M:%S')
    year = obj.year
    month = obj.month
    poll_df = poll_df[(poll_df['Month Index']==month) &
                (poll_df['Year']==year)]
    start_date = min(poll_df['To Date'])
    end_date = max(poll_df['To Date'])
    limits = convert_limits.info(start_date, end_date, poll_df, station)
    if regulator == 'US':
        limits=limits.drop('SA Limits', axis=1)
        limits=limits.rename(columns={'US Limits':'Limits'})
    else:
        limits=limits.drop('US Limits', axis=1)
        limits=limits.rename(columns={'SA Limits':'Limits'})
    return limits


