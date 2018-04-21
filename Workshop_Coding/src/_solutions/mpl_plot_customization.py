## solution matplotlib challenge 
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(X, C, color="green", label="cosine")
ax.plot(X, S, linestyle="--", linewidth=3.5, label="sine")
ax.set_title("My awesome matplotlib figure", size=16)
ax.legend(fontsize=12)
ax.set_xlim([-4,4])
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_yticks([-1, 0, 1])
ax.set_xticklabels(['$-\pi$', '$0$', '$+\pi$'], size=12)
ax.grid()

filepath = "../figures/my_awesome_mpl_figure.png"
fig.savefig(filepath, dpi=300)