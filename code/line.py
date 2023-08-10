import seaborn as sns
import matplotlib.pyplot as plt

from .data import df_skills


statlang = ["python", "r", "spss", "sas", "excel"]


def line_stats():
    df_skills.index = df_skills["date_time"]

    stat_df = df_skills.resample('1M').sum()[statlang]

    ax = plt.stackplot(
        stat_df.index,
        stat_df.azure.values,
        stat_df.aws.values,
        stat_df.bigquery.values,
        stat_df.snowflake.values,
        labels=stat_df)

    ax.legend(loc='upper right')

    return ax
