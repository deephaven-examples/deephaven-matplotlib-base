import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

df = pd.read_csv("/data/auto_clean.csv")


fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection="3d")
ax.scatter3D(
    df["length"],
    df["width"],
    df["height"],
    c=df["peak-rpm"],
    s=df["price"] / 50,
    alpha=0.4,
)
ax.set_xlabel("Length")
ax.set_ylabel("Width")
ax.set_zlabel("Height")
ax.set_title("Relationship between height, weight, and length")
plt.show()
