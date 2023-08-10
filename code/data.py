import pandas as pd


# temp csv file until connection
df = pd.read_csv("mvp/data/transformed/all_data.csv")

df = df[df["date_time"] > '2023-01-01']
df["date_time"] = pd.to_datetime(df["date_time"])

skills = pd.get_dummies(df.tech_tokens.apply(eval).explode())

df_skills = df.join(skills)
