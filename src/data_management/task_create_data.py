import pytask
import pandas as pd
import numpy as np

from src.config import BLD
from src.config import SRC

@pytask.mark.depends_on(SRC / "original_data" / "policy_data.csv")
@pytask.mark.produces(BLD / "data" / "stringency_index_data.csv")
def task_create_data(depends_on, produces):
    """Read the data
    """
    covid_policy= pd.read_csv(depends_on).set_index('indicator')
    """Change datatypes
    """ 
    for col in ['start_date', 'end_date']:
        covid_policy[col]=covid_policy[col].astype('datetime64[ns]')
    """Decompose data for every single day from 2020-02-01 to 2021-02-14 for each indicator
    """
    covid_policy['row'] = range(len(covid_policy))
    starts = covid_policy[['start_date', 'scale', 'flag', 'recorded_flag','maximum', 
                           'row']].rename(columns={'start_date': 'date'})
    ends = covid_policy[['end_date', 'scale', 'flag','recorded_flag','maximum',
                         'row']].rename(columns={'end_date':'date'})
    df_decomp = pd.concat([starts, ends]).set_index('row', append=True)
    df_decomp = df_decomp.groupby(level=[0,1]).apply(lambda x: x.set_index('date').resample('D').fillna(method='pad'))
    df_decomp.reset_index(inplace=True)
    """Long to wide format
    """
    stringency_index=df_decomp.pivot(index="date", columns="indicator", values=["scale","flag","recorded_flag","maximum"])
    stringency_index.columns = ['_'.join(col) for col in stringency_index.columns]
    """Fill missing values
    """
    stringency_index.replace({-100:np.nan},inplace=True)
    """Save the data
    """
    stringency_index.to_csv(produces)