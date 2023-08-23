
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import (axes,axis,title,legend,figure,
                               xlabel,ylabel,xticks,yticks,
                               xscale,yscale,text,grid,
                               plot,scatter,errorbar,hist,polar,
                               contour,contourf,colorbar,clabel,
                               imshow)

df = pd.read_csv("outFile.csv")
sns.scatterplot(x=df.x,
                y=df.y)
plt.title("Initial data")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Initial data")

plt.show()
# After clustering
plt.figure()
df = pd.read_csv("outFileNewAnt.csv")
sns.scatterplot(x=df.x, y=df.y,
                hue=df.c,
                palette=sns.color_palette("hls", n_colors=5))
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
plt.xlabel("x")
plt.ylabel("y")
plt.title("clustering k-means")

plt.show()