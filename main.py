
import pandas as pd
import matplotlib.pyplot as plt  # Corrected import statement for matplotlib
import seaborn as sns
import numpy as np
data = pd.read_csv(r"C:\Users\pravinkuyate\OneDrive\Desktop\grading_system\Dummy_dataset(1).csv")

# Print the entire DataFrame
print(data)
print(data.shape)
print(data.columns)
print(data.nunique())
print(data.info())
# Print the first 3 rows of the DataFrame
print(data.head(3))
print(data.isnull().sum())
print(data['2.Grading Test 1 marks (1 to 25)'].fillna(data['2.Grading Test 1 marks (1 to 25)'].mean(),inplace=True))
data['Sr.no.'].fillna(data['Sr.no.'].mean(),inplace=True)
data['1.Student Name'].fillna('Default Name', inplace=True)
data['3.Grading Test 2 marks (1 to 50)'].fillna(data['3.Grading Test 2 marks (1 to 50)'].mean(),inplace=True)
data['4.Expected marks in Grading Test 3 (1 to 50)'].fillna(data['4.Expected marks in Grading Test 3 (1 to 50)'].mean(),inplace=True)
data['5. Viva marks (1 to 30)'].fillna(data['5. Viva marks (1 to 30)'].mean(),inplace=True)
data['6. Total Attendance (%) out of 100'].fillna(data['6. Total Attendance (%) out of 100'].mean(),inplace=True)
data['7. Trainer Feedback'].fillna(data['7. Trainer Feedback'].mean(),inplace=True)

print(data.isnull().sum())

cat_cols=data.select_dtypes(include=['object']).columns
print(cat_cols)

num_cols=data.select_dtypes(include=np.number).columns.tolist()
print(num_cols)

print(data['6. Total Attendance (%) out of 100'].skew())

missing_percentage = (data.isnull().sum() / len(data)) * 100
print(missing_percentage)

# Drop the column "1.Student Name"
#print(data.drop("1.Student Name", inplace=True, axis=1))

# Calculate correlation matrix
#corr = data.corr()

# Plot the heatmap
#sns.heatmap(corr, vmin=-5, cmap=['green', 'yellow', 'blue', 'red'], vmax=0.6, annot=True)

# Show the plot
#plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming '6. Total Attendance (%) out of 100' and '5. Viva marks (1 to 30)' are valid columns in your DataFrame 'data'
#sns.barplot(y='6. Total Attendance (%) out of 100', x='5. Viva marks (1 to 30)', data=data, palette='PuRd', ci=None)

# Add labels and title
#plt.xlabel('Viva Marks (1 to 30)')
#plt.ylabel('Total Attendance (%) out of 100')
#plt.title('Bar Plot: Total Attendance vs. Viva Marks')

# Show the plot
#plt.show()

for col in num_cols:
    print(col)
    print('Skew:',round(data[col].skew(),2))
    plt.figure(figsize=(15,4))
    plt.subplot(1,2,1)
    data[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1,2,2)
    sns.boxplot(x=data[col])
    plt.show()
