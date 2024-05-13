import pandas as pd
df = pd.read_csv("Exam_table.csv")
mean_concentration = df.groupby("Stage")["Cry1Ac,ppmDW"].mean().reset_index()
print(mean_concentration)
mean_concentration.to_csv("./b2_output1.csv")
#Cry1Ac increased in concentration as it progresses into a late reproductive stage from a vegetative stage. 
