def z_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


plt.figure(figsize=(8, 8))
ax = plt.axes(projection="3d")
x = df["peak-rpm"]
y = df["city-mpg"]
z = z_function(x, y)
ax.plot_trisurf(x, y, z, cmap="viridis", edgecolor="none")
ax.set_xlabel("Peak RPM")
ax.set_ylabel("City-MPG")
ax.set_title("Peak RPM vs City-MPG")
ax.view_init(60, 25)
plt.show()

tri_surf = plt.gcf()
