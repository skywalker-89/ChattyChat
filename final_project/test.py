import pandas as pandasForSortingCSV
import pandas as pd
from csv import writer


# assign dataset
csvData = pandasForSortingCSV.read_csv("final_project/Database/users.csv")

# displaying unsorted data frame
print("\nBefore sorting:")
print(csvData)

# sort data frame
csvData.sort_values(["points"],
                    axis=0,
                    ascending=[False],
                    inplace=True)
df = pd.DataFrame(csvData)
df.to_csv('final_project/Database/sorted_data.csv', mode='a', index=False, header=False)
print("\nAfter sorting:")
print(csvData)