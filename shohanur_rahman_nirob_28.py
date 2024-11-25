import pandas as pd
import matplotlib.pyplot as plt


file_path = "D:/Academic PDF/fifa_ranking_2022.xlsx"  
df = pd.read_excel(file_path, sheet_name='Sheet1')  

plt.plot(df['present_points'],  color="red") 
plt.plot(df['previous_points'], color="green")

plt.xlabel('Teams')
plt.ylabel('Points')
plt.title('Teams present points v/s previous points')
plt.show()