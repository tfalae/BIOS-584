import pandas as pd
import matplotlib.pyplot as plt

ptsd_df = pd.read_excel("data/PTSD dataset.xlsx", sheet_name="main_dataset")

rows, cols = ptsd_df.shape

print("This dataset contains", rows, "rows and", cols, "columns.")

ptsd_col_name = ptsd_df.columns

print("Type before conversion:", type(ptsd_col_name))

ptsd_col_name = list(ptsd_col_name)

print("Type after conversion:", type(ptsd_col_name))

print("Column names:", ptsd_col_name)

print("First item:", ptsd_col_name[0])

print("Index of pcl5_score_intake:", ptsd_col_name.index("pcl5_score_intake"))

print("Descriptive stats (direct column call):")
print(ptsd_df["pcl5_score_intake"].describe())

print("\nDescriptive stats (using ptsd_col_name):")
col_index = ptsd_col_name.index("pcl5_score_intake")
print(ptsd_df[ptsd_col_name[col_index]].describe())

import matplotlib.pyplot as plt

age = ptsd_df["age_iop"]        # Age column
pcl5_score_intake = ptsd_df["pcl5_score_intake"]  # PCL5 Score at Intake column

plt.scatter(age, pcl5_score_intake)

plt.xlabel("Age")
plt.ylabel("PCL5 Score at Intake")
plt.title("Scatter Plot")

plt.show()

freq_table = ptsd_df["gender_code"].value_counts()

print("Frequency table of gender_code:")
print(freq_table)

contingency_table = pd.crosstab(ptsd_df["gender_code"], ptsd_df["race_code"])

print("Contingency table between gender_code and race_code:")
print(contingency_table)
