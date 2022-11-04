df["body-style"].unique()

df["body_style1"] = df["body-style"].replace(
    {"convertible": 1, "hatchback": 2, "sedan": 3, "wagon": 4, "hardtop": 5}
)

gr = df.groupby("body_style1")["peak-rpm", "price"].agg("mean")
x = gr.index
y = gr["peak-rpm"]
z = [0] * 5
colors = ["b", "g", "crimson", "r", "pink"]
dx = 0.3 * np.ones_like(z)
dy = [30] * 5
dz = gr["price"]
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_xticklabels(["convertible", "hatchback", "sedan", "wagon", "hardtop"])
ax.set_xlabel("Body Style", labelpad=7)
ax.set_yticks(np.linspace(5000, 5250, 6))
ax.set_ylabel("Peak Rpm", labelpad=10)
ax.set_zlabel("Price")
ax.set_zticks(np.linspace(7000, 22250, 6))
ax.set_title("Change of Price with Body_style and Peak RPM")
ax.bar3d(x, y, z, dx, dy, dz)
