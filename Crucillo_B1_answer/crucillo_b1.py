import pandas as pd
df = pd.read_csv("Exam_Table.csv")
output = df[df["Entry"] == "M4"]
print (output)
output.to_csv("./b1_output1.csv")
