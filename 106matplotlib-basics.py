import matplotlib.pyplot as plt
import numpy as np

# x=[1,2,3,4]
# y=[1,4,9,16]

# # plt.plot(x,y,color="red",linewidth="5")
# # plt.plot(x,y,"--g")#green dashed line
# # plt.plot(x,y,"o--r")#marker red dahed line
# plt.axis([0,6,0,20])
# plt.title("Grafik Başlığı")
# plt.xlabel("x label")
# plt.ylabel("y label")

# x=np.linspace(0,2,100)

# plt.plot(x,x,label="linear",color="red")
# plt.plot(x,x**2,label="quadratic",color="yellow")
# plt.plot(x,x**3,label="cubic",color="green")

# plt.xlabel("x label")
# plt.ylabel("y label")

# plt.title("Simple Plot")

# plt.legend()

'''

x=np.linspace(0,2,100)

fig,axs=plt.subplots(3)

axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="green") 
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="blue") 
axs[2].set_title("cubic")


plt.tight_layout()
'''
'''
x=np.linspace(0,2,100)

fig,axs=plt.subplots(2,2)
fig.suptitle("grafik başlığı")


axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")
'''

import pandas as pd

df=pd.read_csv("datasets/nba.csv")

df=df.drop(["Number"],axis=1).groupby("Team").mean("Team")

df.head().plot(subplots=True)

plt.legend()

plt.show()
