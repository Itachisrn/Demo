import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
file_path = "D:/Academic PDF/fifa_ranking_2022.xlsx"  # Replace with your file path
df = pd.read_excel(file_path, sheet_name='Sheet1')  # Replace 'Sheet1' with your sheet name

# Convert DataFrame to a NumPy array
array_data = df.to_numpy()

# Alternatively, convert DataFrame to a list of lists
list_data = df.values.tolist()

# Print the results
print("Array form:")
print(array_data)

print("\nList form:")
print(list_data)

# Convert a specific column to a set
column_set = set(df['team'])  ## Replace 'ColumnName' with the actual column name

print("\nSet form:")
print(column_set)

#names_set = set(df[''])  # You can change 'Name' to any column you want
#print("Set of Names:")
#print(names_set)

# Convert DataFrame to a dictionary
dict_data = df.to_dict(orient='list')  # 'list' will create a dictionary with column names as keys

print("\nDictionary form:")
print(dict_data)

# Convert DataFrame to a list of tuples
tuple_data = [tuple(row) for row in df.to_numpy()]

print("\nTuple form:")
print(tuple_data)


# Plotting
# Let's plot Age vs Height

#plt.bar(df['team'], df['rank'], color='skyblue')
#plt.pie(df['rank'], labels=df['team'] ) #color='skyblue')
plt.scatter(df['team'], df['rank'])
plt.xlabel('Teams')
plt.ylabel('rank')
plt.title('Height of Individuals')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
plt.show()