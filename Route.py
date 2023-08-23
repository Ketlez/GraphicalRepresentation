
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import (axes,axis,title,legend,figure,
                               xlabel,ylabel,xticks,yticks,
                               xscale,yscale,text,grid,
                               plot,scatter,errorbar,hist,polar,
                               contour,contourf,colorbar,clabel,
                               imshow)
df1 = pd.read_csv("outFilePathAnt.csv")

df2 = pd.read_csv("outFilePathKmeans.csv")

plt.show()

# After clustering
plt.figure()
df = pd.read_csv("outFileNewAnt.csv")
sns.scatterplot(x=df.x, y=df.y,
                hue=df.c,
                palette=sns.color_palette("hls", n_colors=5))
for i in range(0, len(df1.x)):
    plt.plot(df1.x, df1.y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("clustering by the ant algorithm")

plt.show()

# After clustering
plt.figure()
df = pd.read_csv("outFileNewKmeans.csv")
sns.scatterplot(x=df.x, y=df.y,
                hue=df.c,
                palette=sns.color_palette("hls", n_colors=5))
for i in range(0, len(df2.x)):
    plt.plot(df2.x, df2.y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("clustering k-means")

plt.show()