import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
#x=np.array(["Satur", "sun", "Mon", "tue", "Fri"])
x=np.array([10/80, 2/80, 7/80, 15/80, 7/80])
y = np.array([10, 2, 7, 15, 7])
y1 = np.array([17, 13, 5, 4, 14])
clrs = np.array(["green", "red", "purple", "black", "blue"])
# For plot
plt.plot(y, color="red", marker="+") #linestyle = "dashdot"
#plt.plot(y1, color="black", marker="o")

#plt.xticks([2,5,10,18])
#plt.yticks([0,3,12,17])

# For Bar Diagram

#plt.barh(y,x, color="black")
#plt.barh(y1,x, color="blue")

# For Pie Chart

#plt.pie(y,labels=x, startangle=22, shadow=True, colors=clrs, radius=1.4)

# For Scatter 

#plt.scatter(x,y)

plt.xlabel("Time")
plt.ylabel("Speed")

#plt.xticks(["Satur", "sun", "Mon", "tue", "Fri"])


plt.title("Testing")
plt.show()
