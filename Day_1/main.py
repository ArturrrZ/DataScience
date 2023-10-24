import pandas
#pip install
df = pandas.read_csv("salaries_by_college_major.csv")
# print(df)

first_5_rows=df.head()
# print(first_5_rows)

last_5_rows=df.tail()
# print(last_5_rows)

shape=df.shape
# print(shape)
# print(type(shape))


check_for_nan=df.isna
# print(check_for_nan)

clear_df_without_nan=df.dropna()
# print(clear_df_without_nan.tail())
# print(clear_df_without_nan.shape)

