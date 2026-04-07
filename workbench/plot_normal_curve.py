import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft YaHei", "SimHei", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False


def normal_pdf(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


fig, ax = plt.subplots(figsize=(12, 7), dpi=150)

x = np.linspace(-4, 4, 1000)
y = normal_pdf(x, 0, 1)

ax.plot(x, y, color="#2C3E50", linewidth=3, label="标准正态分布")

ax.fill_between(x, y, alpha=0.3, color="#3498DB", label="概率密度")

ax.fill_between(
    x[x <= -1.96], y[x <= -1.96], alpha=0.5, color="#E74C3C", label="临界区域 (α=0.05)"
)
ax.fill_between(x[x >= 1.96], y[x >= 1.96], alpha=0.5, color="#E74C3C")

ax.axvline(
    x=0, color="#27AE60", linestyle="--", linewidth=2, alpha=0.8, label="均值 μ=0"
)
ax.axvline(x=1, color="#F39C12", linestyle=":", linewidth=2, alpha=0.8, label="σ=1")
ax.axvline(x=-1, color="#F39C12", linestyle=":", linewidth=2, alpha=0.8)

ax.annotate(
    "μ=0",
    xy=(0, 0.4),
    xytext=(0, 0.45),
    fontsize=12,
    ha="center",
    fontweight="bold",
    color="#27AE60",
    arrowprops=dict(arrowstyle="->", color="#27AE60", lw=1.5),
)

ax.annotate(
    "σ=1",
    xy=(1, 0.24),
    xytext=(1.5, 0.28),
    fontsize=11,
    ha="center",
    color="#F39C12",
    arrowprops=dict(arrowstyle="->", color="#F39C12", lw=1.5),
)

ax.annotate(
    "W 值越接近 1\n表示与理论正态曲线\n拟合程度越高",
    xy=(2.5, 0.15),
    xytext=(2.5, 0.15),
    fontsize=10,
    ha="left",
    color="#2C3E50",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#ECF0F1", edgecolor="#BDC3C7"),
)

ax.set_xlabel("标准差 (z)", fontsize=13, fontweight="bold", labelpad=10)
ax.set_ylabel("概率密度", fontsize=13, fontweight="bold", labelpad=10)
ax.set_title(
    "标准正态分布曲线\n（Shapiro-Wilk 正态性检验示意）",
    fontsize=15,
    fontweight="bold",
    pad=20,
    color="#2C3E50",
)

ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.45)
ax.set_xticks(np.arange(-4, 5, 1))
ax.set_yticks([])

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_linewidth(1.5)

ax.legend(loc="upper right", fontsize=10, framealpha=0.9)

ax.text(
    0.02,
    0.98,
    "N(0, 1)",
    transform=ax.transAxes,
    fontsize=14,
    fontweight="bold",
    va="top",
    color="#8E44AD",
)

plt.tight_layout()
plt.savefig(
    "figures/normal-curve.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
)
plt.close()

print("Image saved: figures/normal-curve.png")
