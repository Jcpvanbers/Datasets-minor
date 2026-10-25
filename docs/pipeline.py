"""Genereert docs/pipeline.png: de lokale en de online pipeline van dit project.

Opnieuw genereren:  python docs/pipeline.py
De gebruikte packages (matplotlib) staan in environment.yml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Kleuren per rol: (vulling, rand)
KLEUREN = {
    "data": ("#E8F1FB", "#2F6FB3"),      # bestanden op schijf
    "proces": ("#E9F6EC", "#2E7D4F"),    # notebook / verwerking
    "werk": ("#FFF3E0", "#C77700"),      # werkkopie op de runtime
    "domein": ("#E6F4F3", "#0F766E"),    # eigen domein
    "rapport": ("#F1EAFB", "#6B3FA0"),   # dashboard / Power BI
}

TEKST = "#111827"
GRIJS = "#4B5563"
LANE = "#F7F8FA"
LANE_RAND = "#D5D9E0"
PIJL = "#6B7280"

fig = plt.figure(figsize=(15, 9), dpi=180)
fig.patch.set_facecolor("white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")


def lane(y0, hoogte, label):
    ax.add_patch(
        FancyBboxPatch(
            (2, y0), 96, hoogte,
            boxstyle="round,pad=0,rounding_size=1.6",
            fc=LANE, ec=LANE_RAND, lw=1.0, zorder=0,
        )
    )
    ax.text(4.5, y0 + hoogte - 2.2, label, fontsize=8.4, color="#6B7280",
            fontweight="bold", va="center", zorder=1)


def box(x, y, w, h, titel, sub, soort):
    fc, ec = KLEUREN[soort]
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0,rounding_size=1.1",
            fc=fc, ec=ec, lw=1.3, zorder=2,
        )
    )
    ax.text(x + w / 2, y + h * 0.64, titel, ha="center", va="center",
            fontsize=10.2, fontweight="bold", color=TEKST, zorder=3)
    if sub:
        ax.text(x + w / 2, y + h * 0.30, sub, ha="center", va="center",
                fontsize=7.5, color=GRIJS, zorder=3)


def pijl(start, eind, label=None, label_xy=None, ha="center"):
    ax.annotate(
        "", xy=eind, xytext=start,
        arrowprops=dict(arrowstyle="-|>", color=PIJL, lw=1.4,
                        shrinkA=0, shrinkB=0, mutation_scale=13),
        zorder=1,
    )
    if label and label_xy:
        ax.text(*label_xy, label, ha=ha, va="center", fontsize=7.4,
                color=GRIJS, linespacing=1.15, zorder=4,
                bbox=dict(fc="white", ec="none", pad=1.0))


def elleboog(x_split, y_van, y_naar, x_eind):
    ax.plot([x_split - 2.7, x_split], [y_van, y_van], color=PIJL, lw=1.4, zorder=1)
    ax.plot([x_split, x_split], [y_van, y_naar], color=PIJL, lw=1.4, zorder=1)
    ax.annotate(
        "", xy=(x_eind, y_naar), xytext=(x_split, y_naar),
        arrowprops=dict(arrowstyle="-|>", color=PIJL, lw=1.4,
                        shrinkA=0, shrinkB=0, mutation_scale=13),
        zorder=1,
    )


# ---------------------------------------------------------------- kop
ax.text(50, 97.2, "Datasets minor — de twee pipelines", ha="center", va="center",
        fontsize=19, fontweight="bold", color=TEKST)
ax.text(50, 93.4,
        "Zelfde opschoning, dezelfde assert-validaties en dezelfde negen tabellen — twee routes naar hetzelfde resultaat.",
        ha="center", va="center", fontsize=10, color=GRIJS)

legend = [
    (27, "data", "bestanden"),
    (35, "proces", "verwerking"),
    (45, "werk", "werkkopie"),
    (54, "domein", "domein"),
    (62, "rapport", "rapportage"),
]
for x, soort, tekst in legend:
    fc, ec = KLEUREN[soort]
    ax.add_patch(
        FancyBboxPatch((x, 89.7), 1.4, 1.4, boxstyle="round,pad=0,rounding_size=0.3",
                       fc=fc, ec=ec, lw=1.0, zorder=3)
    )
    ax.text(x + 2.2, 90.4, tekst, va="center", fontsize=8, color=GRIJS, zorder=3)

# ---------------------------------------------------------------- lokaal
lane(54.5, 33.5, "LOKAAL · bestanden in de repo · geen internet of account nodig")

box(4, 70, 17, 11, "Lokaal/Data", "10 CSV's (sales niet in Git)", "data")
box(26, 70, 20, 11, "Notebook 1 · lokaal", "analyse · opschonen · valideren", "proces")
box(51, 70, 17, 11, "Lokaal/PQ", "9 parquet-bestanden", "data")
box(73, 77.5, 22, 9, "Dashboard lokaal", "2 Dash-apps · 8050 / 8051", "rapport")
box(73, 59, 22, 9, "Power BI lokaal", "Contoso dashboard Lokaal.pbix", "rapport")

pijl((21, 75.5), (26, 75.5), "lezen", (23.5, 77.5))
pijl((46, 75.5), (51, 75.5), "schrijven", (48.5, 77.5))
elleboog(70.7, 75.5, 81.5, 73)
elleboog(70.7, 75.5, 63.5, 73)

# ---------------------------------------------------------------- online
lane(9.5, 39.5, "ONLINE · bron en bestemming op het domein · werkkopie lokaal")

# runtime-omgeving (waar de werkkopie staat)
box(3, 34, 15, 11, "Domein", "CSV's · contoso-data", "domein")
box(22, 34, 18, 11, "Notebook 1 · online", "analyse · opschonen · valideren", "proces")
box(44, 34, 14, 11, "PQ/ werkkopie", "to_parquet", "werk")
box(62, 34, 26, 11, "Domein /PQ", "9 parquet-bestanden", "domein")
box(59, 13, 14.5, 11, "Dashboard online", "2 Dash-apps\n8050 / 8051", "rapport")
box(75, 13, 14.5, 11, "Power BI online", "Contoso dashboard\nOnline.pbix", "rapport")

pijl((18, 39.5), (22, 39.5), "HTTPS\n(reader)", (20, 41.4))
pijl((40, 39.5), (44, 39.5), "schrijven", (42, 41.4))
pijl((58, 39.5), (62, 39.5), "SFTP\n(uploader)", (60, 41.4))
pijl((66.25, 34), (66.25, 24))
pijl((82.25, 34), (82.25, 24))
ax.text(74.25, 27.8, "HTTPS\n(reader)", ha="center", va="center", fontsize=7.4,
        color=GRIJS, linespacing=1.15, zorder=4,
        bbox=dict(fc="white", ec="none", pad=1.0))

ax.text(4.5, 19.2, "De werkkopie is alleen een tussenstap:\nde bron en het eindresultaat staan op het domein.",
        ha="left", va="center", fontsize=7.8, color="#6B7280", linespacing=1.5)

ax.text(50, 5.6,
        "Online: upload via tijdelijk bestand, groottecheck en atomaire rename; de CSV's op het domein blijven ongewijzigd.",
        ha="center", va="center", fontsize=7.6, color=GRIJS)

doel = Path(__file__).with_name("pipeline.png")
fig.savefig(doel, dpi=180, facecolor="white")
print(f"geschreven: {doel}")
